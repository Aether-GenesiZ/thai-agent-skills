import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('package', Path(__file__).resolve().parents[1] / 'scripts/package.py')
package = importlib.util.module_from_spec(spec)
spec.loader.exec_module(package)

class PackageTests(unittest.TestCase):
    def test_untracked_secret_excluded_and_tracked_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            subprocess.run(['git', 'init', '-q', str(root)], check=True)
            (root / 'skills').mkdir()
            (root / 'skills/SKILL.md').write_text('public')
            (root / 'skills/.env').write_text('synthetic untracked secret')
            subprocess.run(['git', '-C', str(root), 'add', 'skills/SKILL.md'], check=True)
            self.assertEqual([f.name for f in package.distribution_files(root)], ['SKILL.md'])
            link = root / 'skills/private-link'
            try:
                link.symlink_to(root / 'skills/.env')
            except OSError:
                return  # Windows without symlink privileges: exclusion still checked.
            subprocess.run(['git', '-C', str(root), 'add', 'skills/private-link'], check=True)
            with self.assertRaises(ValueError):
                package.distribution_files(root)
