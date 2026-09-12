from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).parents[1] / "scripts" / "check_readme_index.py"


class ReadmeIndexCheckerTests(unittest.TestCase):
    def run_checker(self, root: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(root)],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_complete_readme_index_passes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "prompts").mkdir()
            (root / "prompts" / "example.md").write_text("# Example\n", encoding="utf-8")
            (root / "README.md").write_text(
                "[Example](prompts/example.md)\n", encoding="utf-8"
            )

            result = self.run_checker(root)

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_readme_entry_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "prompts").mkdir()
            (root / "prompts" / "unlisted.md").write_text("# Unlisted\n", encoding="utf-8")
            (root / "README.md").write_text("# Catalog\n", encoding="utf-8")

            result = self.run_checker(root)

            self.assertEqual(result.returncode, 1)
            self.assertIn("prompts/unlisted.md", result.stdout)


if __name__ == "__main__":
    unittest.main()
