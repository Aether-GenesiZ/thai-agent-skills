#!/usr/bin/env python3
"""Build a portable zip using only repository-owned distribution files."""
import json
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT/'.claude-plugin/plugin.json').read_text())
output = ROOT/'dist'/f"{manifest['name']}-{manifest['version']}.zip"
output.parent.mkdir(exist_ok=True)
include = ['skills','scripts','licenses','.claude-plugin','tests','docs',
           'README.md','LICENSE','THIRD_PARTY_NOTICES.md','sources.json','plugin.json',
           'evals/smoke-prompt.txt','evals/verification.json']
with ZipFile(output,'w',ZIP_DEFLATED) as archive:
    for entry in include:
        path = ROOT/entry
        files = [path] if path.is_file() else sorted(path.rglob('*'))
        for file in files:
            if file.is_file() and '__pycache__' not in file.parts:
                archive.write(file,file.relative_to(ROOT).as_posix())
print(output)
