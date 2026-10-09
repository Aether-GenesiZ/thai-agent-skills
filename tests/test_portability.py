import importlib.util
from pathlib import Path
import tempfile
import unittest
from datetime import date

ROOT = Path(__file__).resolve().parents[1]

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

installer = load('installer', ROOT / 'scripts/install.py')
dates = load('dates', ROOT / 'skills/thai-date-format/convert.py')

class InstallerTests(unittest.TestCase):
    def test_install_check_idempotence_and_edited_file_protection(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'harness with spaces/skills'
            installer.install([target])
            installer.install([target], check=True)
            installer.install([target])
            f = target / 'thai-language/SKILL.md'
            edited = f.read_text() + '\nUser customization\n'
            f.write_text(edited)
            with self.assertRaises(ValueError):
                installer.install([target])
            self.assertEqual(f.read_text(), edited)

    def test_all_targets_preflight_before_writes(self):
        with tempfile.TemporaryDirectory() as tmp:
            first, second = Path(tmp)/'first', Path(tmp)/'second'
            foreign = second/'thai-language'
            foreign.mkdir(parents=True)
            (foreign/'SKILL.md').write_text('foreign content')
            with self.assertRaises(ValueError):
                installer.install([first, second])
            self.assertFalse(first.exists())
            self.assertEqual((foreign/'SKILL.md').read_text(), 'foreign content')

    def test_missing_detection_and_dry_run(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)/'skills'
            installer.install([target], dry_run=True)
            self.assertFalse(target.exists())
            with self.assertRaises(ValueError):
                installer.install([target], check=True)

    def test_uninstall_preserves_unrelated_files_and_rejects_edits(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)/'skills'
            installer.install([target])
            unrelated = target/'unrelated.txt'
            unrelated.write_text('keep')
            file = target/'thai-language/SKILL.md'
            original = file.read_text()
            file.write_text(original+'edited')
            with self.assertRaises(ValueError):
                installer.uninstall([target])
            file.write_text(original)
            installer.uninstall([target])
            self.assertEqual(unrelated.read_text(), 'keep')
            self.assertFalse((target/'thai-language').exists())

    def test_source_target_rejected(self):
        with self.assertRaises(ValueError):
            installer.install([ROOT/'skills'])

class DateTests(unittest.TestCase):
    def test_explicit_era_takes_precedence(self):
        self.assertEqual(dates.parse_thai_date('16 พ.ค. ค.ศ. 2569'), date(2569,5,16))
        self.assertEqual(dates.parse_thai_date('16 พ.ค. พ.ศ. 2300'), date(1757,5,16))
        self.assertEqual(dates.parse_thai_date('๑๖ พ.ค. พ.ศ. ๒๕๖๙'), date(2026,5,16))

    def test_invalid_dates_and_trailing_junk_rejected(self):
        for text in ['31/02/2569','29/02/2569','16/13/2569','0/05/2569',
                     '16 พ.ค. ค.ศ. 26','16/05/2569junk']:
            with self.subTest(text=text), self.assertRaises(ValueError):
                dates.parse_thai_date(text)

if __name__ == '__main__':
    unittest.main()
