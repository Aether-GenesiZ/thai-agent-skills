#!/usr/bin/env python3
"""Build a portable zip from explicitly allowed Git-tracked distribution files."""
import json
from pathlib import Path
import subprocess
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
DIRECTORIES = {'skills', 'scripts', 'licenses', '.claude-plugin', 'tests', 'docs'}
FILES = {'README.md', 'LICENSE', 'THIRD_PARTY_NOTICES.md', 'sources.json',
         'plugin.json', 'CONTRIBUTING.md', 'SECURITY.md', 'SUPPORT.md',
         'CODE_OF_CONDUCT.md', 'CHANGELOG.md', 'AGENTS.md', 'package.json',
         'package-lock.json', 'evals/smoke-prompt.txt', 'evals/verification.json'}


def distribution_files(root):
    tracked = subprocess.check_output(['git', 'ls-files', '-z'], cwd=root).decode().split('\0')
    selected = []
    for name in sorted(filter(None, tracked)):
        relative = Path(name)
        if relative.parts[0] not in DIRECTORIES and name not in FILES:
            continue
        file = root / relative
        if any((root / Path(*relative.parts[:i])).is_symlink()
               for i in range(1, len(relative.parts) + 1)):
            raise ValueError(f'Symlinks are not distributable: {name}')
        if root.resolve() not in file.resolve().parents:
            raise ValueError(f'Path escapes repository: {name}')
        if any(part.startswith('.env') or part == '__pycache__' for part in relative.parts) or file.suffix in {'.pem', '.key', '.bundle'}:
            raise ValueError(f'Sensitive or generated file is not distributable: {name}')
        if not file.is_file():
            raise ValueError(f'Tracked file is missing: {name}')
        selected.append(file)
    return selected


def main():
    manifest = json.loads((ROOT / '.claude-plugin/plugin.json').read_text())
    files = distribution_files(ROOT)
    output = ROOT / 'dist' / f"{manifest['name']}-{manifest['version']}.zip"
    output.parent.mkdir(exist_ok=True)
    with ZipFile(output, 'w', ZIP_DEFLATED) as archive:
        for file in files:
            archive.write(file, file.relative_to(ROOT).as_posix())
    print(output)


if __name__ == '__main__':
    main()
