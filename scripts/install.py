#!/usr/bin/env python3
"""Copy portable skills into harness discovery directories without clobbering files."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile

ROOT = Path(__file__).resolve().parent.parent
RECEIPT = '.thai-agent-skills-install.json'


def digest(folder: Path) -> str:
    h = hashlib.sha256()
    for file in sorted(folder.rglob('*')):
        if file.is_file() and '__pycache__' not in file.parts:
            h.update(file.relative_to(folder).as_posix().encode())
            h.update(b'\0')
            h.update(file.read_bytes())
    return h.hexdigest()


def defaults(home: Path) -> dict[str, Path]:
    return {
        'agy': home / '.gemini/antigravity-cli/skills',
        'claude': Path(os.environ.get('CLAUDE_CONFIG_DIR', str(home / '.claude'))) / 'skills',
        'hermes': Path(os.environ.get('HERMES_HOME', str(home / '.hermes'))) / 'skills',
        'codex': Path(os.environ.get('CODEX_HOME', str(home / '.codex'))) / 'skills',
    }


def install(targets: list[Path], *, check: bool = False, dry_run: bool = False) -> list[dict]:
    sources = sorted(d for d in (ROOT / 'skills').iterdir() if (d / 'SKILL.md').is_file())
    plans = []
    # Preflight ALL destinations before changing any of them.
    for target in dict.fromkeys(t.expanduser().absolute() for t in targets):
        if target.is_symlink():
            target = target.resolve()
        if target == ROOT / 'skills' or ROOT in target.parents:
            raise ValueError('Installation target cannot be inside the source repository')
        receipt_path = target / RECEIPT
        old = json.loads(receipt_path.read_text()) if receipt_path.exists() else {}
        if old and old.get('package') != 'thai-agent-skills':
            raise ValueError(f'Foreign receipt: {receipt_path}')
        files = old.get('skills', {})
        for source in sources:
            dest = target / source.name
            expected = digest(source)
            exists = dest.exists() or dest.is_symlink()
            if exists:
                if dest.is_symlink() or not dest.is_dir():
                    raise ValueError(f'Refusing conflicting path: {dest}')
                actual = digest(dest)
                if actual != expected and files.get(source.name) != actual:
                    raise ValueError(f'Refusing to overwrite unowned or edited skill: {dest}')
            else:
                actual = None
            if check and actual != expected:
                raise ValueError(f'Missing or outdated skill: {dest}')
            plans.append((target, source, dest, expected, actual))
    reports = []
    for target in dict.fromkeys(p[0] for p in plans):
        selected = [p for p in plans if p[0] == target]
        if not check and not dry_run:
            target.mkdir(parents=True, exist_ok=True)
            for _, source, dest, expected, actual in selected:
                if expected == actual:
                    continue
                staging = Path(tempfile.mkdtemp(prefix='.thai-stage-', dir=target))
                backup = staging / 'old'
                payload = staging / 'payload'
                try:
                    shutil.copytree(source, payload, ignore=shutil.ignore_patterns('__pycache__'))
                    if dest.exists():
                        dest.rename(backup)
                    try:
                        payload.rename(dest)
                    except Exception:
                        if backup.exists():
                            backup.rename(dest)
                        raise
                finally:
                    shutil.rmtree(staging)
            receipt = {'package':'thai-agent-skills', 'version':json.loads((ROOT / '.claude-plugin/plugin.json').read_text())['version'],
                       'source':str(ROOT), 'skills':{s.name:e for _,s,_,e,_ in selected}}
            with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=target,
                                             prefix='.thai-receipt-', delete=False) as f:
                json.dump(receipt, f, indent=2)
                temp = Path(f.name)
            temp.replace(target / RECEIPT)
        reports.append({'target':str(target), 'skills':len(selected),
                        'status':'checked' if check else 'dry-run' if dry_run else 'installed'})
    return reports


def uninstall(targets: list[Path], *, dry_run: bool = False) -> list[dict]:
    plans = []
    for target in dict.fromkeys(t.expanduser().absolute() for t in targets):
        receipt_path = target / RECEIPT
        if not receipt_path.is_file():
            raise ValueError(f'No owned installation receipt: {target}')
        receipt = json.loads(receipt_path.read_text())
        if receipt.get('package') != 'thai-agent-skills':
            raise ValueError(f'Foreign receipt: {receipt_path}')
        for name, expected in receipt['skills'].items():
            if Path(name).name != name or name in ('.', '..'):
                raise ValueError(f'Invalid receipt skill name: {name}')
            dest = target / name
            if dest.is_symlink() or not dest.is_dir() or digest(dest) != expected:
                raise ValueError(f'Refusing to remove modified or missing skill: {dest}')
            plans.append(dest)
    if not dry_run:
        for dest in plans:
            shutil.rmtree(dest)
        for target in dict.fromkeys(d.parent for d in plans):
            (target / RECEIPT).unlink()
    return [{'target':str(t), 'status':'dry-run' if dry_run else 'uninstalled'} for t in targets]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--harness', nargs='+', choices=['all','agy','claude','hermes','codex'], default=[])
    parser.add_argument('--target', action='append', type=Path, default=[], help='Any harness skill directory; repeatable')
    parser.add_argument('--home', type=Path, default=Path.home(), help='Home directory for default harness paths')
    parser.add_argument('--uninstall', action='store_true', help='Remove only unchanged skills recorded by this installer')
    parser.add_argument('--check', action='store_true', help='Verify installed contents without writing')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    mappings = defaults(args.home)
    harnesses = list(mappings) if 'all' in args.harness else args.harness
    targets = args.target + [mappings[h] for h in harnesses]
    if not targets:
        parser.error('Choose --harness all or --target DIR')
    try:
        if args.uninstall and args.check:
            parser.error('--uninstall and --check cannot be combined')
        result = uninstall(targets, dry_run=args.dry_run) if args.uninstall else install(targets, check=args.check, dry_run=args.dry_run)
        print(json.dumps(result, indent=2))
        return 0
    except (ValueError, OSError) as e:
        print(f'Install failed: {e}', file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(main())
