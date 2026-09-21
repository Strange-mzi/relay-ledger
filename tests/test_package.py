"""Regression checks for broken releases; these are not model evaluations."""

from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_package import ROOT, SKILL, check


class PackageChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "package"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__", "dist"))

    def append_entry(self, text):
        with (self.root / SKILL).open("a", encoding="utf-8") as file:
            file.write(text)

    def test_release_is_valid(self):
        self.assertEqual([], check(self.root))

    def test_missing_role_reference_fails(self):
        (self.root / "skills/relay-ledger/references/review.md").unlink()
        self.assertTrue(any("Broken link" in error for error in check(self.root)))

    def test_outside_link_fails(self):
        self.append_entry("\n[private](../../../outside.md)\n")
        self.assertTrue(any("escapes package" in error for error in check(self.root)))

    def test_context_expansion_fails(self):
        self.append_entry("\n" + "extra " * 1000)
        self.assertTrue(any("context ceiling" in error for error in check(self.root)))

    def test_local_path_leak_fails(self):
        self.append_entry("\nPrivate checkout: /home/example/project\n")
        self.assertTrue(any("Machine-specific" in error for error in check(self.root)))

    def test_wrong_skill_identity_fails(self):
        entry = self.root / SKILL
        entry.write_text(entry.read_text(encoding="utf-8").replace("name: relay-ledger", "name: different"), encoding="utf-8")
        self.assertTrue(any("name must match" in error for error in check(self.root)))


if __name__ == "__main__":
    unittest.main()
