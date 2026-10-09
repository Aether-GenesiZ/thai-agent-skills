#!/usr/bin/env python3
"""Run small real-model smoke tasks; requires installed/authenticated harness CLIs."""
import argparse
import json
import subprocess
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def extract(text):
    decoder = json.JSONDecoder()
    # Accept plain/fenced model JSON and CLI envelopes without evaluating strings.
    for i, char in enumerate(text):
        if char != '{':
            continue
        try:
            obj, _ = decoder.raw_decode(text[i:])
        except ValueError:
            continue
        if isinstance(obj, dict) and 'skill_loaded' in obj:
            return obj
        if isinstance(obj, dict):
            for key in ('result', 'response', 'text'):
                if isinstance(obj.get(key), str):
                    candidate = extract(obj[key])
                    if candidate:
                        return candidate
            if isinstance(obj.get("item"), dict) and isinstance(obj["item"].get("text"), str):
                candidate = extract(obj["item"]["text"])
                if candidate:
                    return candidate
    return None


def checks(obj):
    failures = []
    if not obj or obj.get('skill_loaded') != 'thai-language':
        return ['Expected structured response naming thai-language']
    for field in ('rule','thai','translation','ui'):
        if not isinstance(obj.get(field), str) or not obj[field].strip():
            failures.append(f'Missing text: {field}')
    text = obj.get('thai', '')
    if 'ศุกร์' not in text or 'ลูกค้า' not in text or not any(x in text for x in ['ยังไม่','อย่าเพิ่ง']):
        failures.append('Team message must preserve Friday deadline and do-not-send-yet constraint')
    if 'ส่งกลับ' in text:
        failures.append('Added an unrequested return-delivery action')
    if 'ครับ' in text or 'ค่ะ' in text:
        failures.append('Team message requested neutral phrasing without gendered particles')
    translation = obj.get('translation','')
    if not all(x in translation for x in ['ก่อนวันศุกร์','ต้อง','ใบเสร็จ']):
        failures.append('Translation must preserve before Friday, obligation and receipt')
    if obj.get('ui') not in ('บันทึกไม่ได้','ไม่สามารถบันทึกได้','บันทึกไม่สำเร็จ'):
        failures.append('UI should convey failed save')
    return failures


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--harness', nargs='+', choices=['claude','codex','hermes','agy'], required=True)
    parser.add_argument('--timeout', type=int, default=240)
    args = parser.parse_args()
    prompt = (ROOT/'evals/smoke-prompt.txt').read_text()
    results = ROOT/'evals/results'; results.mkdir(exist_ok=True)
    reports = []
    with tempfile.TemporaryDirectory(prefix='thai-skills-smoke-') as cwd:
        for name in args.harness:
            output = results/f'{name}-output.md'
            commands = {
                'claude': ['claude','-p',prompt,'--output-format','json','--no-session-persistence',
                           '--permission-mode','plan','--tools','Read,Skill','--setting-sources','user'],
                'codex': ['codex','exec','--skip-git-repo-check','--ephemeral','--sandbox','read-only',
                          '--json','-o',str(output),prompt],
                'hermes': ['hermes','-s','thai-language','-t','skills','-z',prompt],
                'agy': ['agy','--print-timeout',f'{args.timeout}s','--output-format','json','-p',prompt],
            }
            started = time.monotonic()
            try:
                run = subprocess.run(commands[name],cwd=cwd,stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT,text=True,timeout=args.timeout)
                raw = run.stdout
                (results/f'{name}.log').write_text(raw)
                obj = extract(raw)
                errors = checks(obj)
                if run.returncode:
                    errors.insert(0,f'CLI exit code {run.returncode}')
                reports.append({'harness':name,'exit_code':run.returncode,
                                'elapsed_seconds':round(time.monotonic()-started,1),
                                'status':'passed' if not errors else 'failed',
                                'issues':errors,'response':obj})
            except subprocess.TimeoutExpired as e:
                raw = e.stdout or b''
                (results/f'{name}.log').write_text(raw.decode(errors='replace') if isinstance(raw,bytes) else raw)
                reports.append({'harness':name,'status':'timeout'})
            except OSError as e:
                reports.append({'harness':name,'status':'unavailable','error':str(e)})
            print(json.dumps(reports[-1],ensure_ascii=False),flush=True)
    (results/'summary.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2)+'\n')
    return 0 if all(r['status']=='passed' for r in reports) else 1

if __name__ == '__main__':
    raise SystemExit(main())
