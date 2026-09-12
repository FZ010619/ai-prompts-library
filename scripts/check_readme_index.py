from pathlib import Path
import sys


def missing_prompt_links(root: Path) -> list[str]:
    readme = (root / "README.md").read_text(encoding="utf-8")
    prompt_directory = root / "prompts"
    return [
        path.relative_to(root).as_posix()
        for path in sorted(prompt_directory.glob("*.md"))
        if path.relative_to(root).as_posix() not in readme
    ]


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).parents[1]
    missing = missing_prompt_links(root)
    if missing:
        print("README.md is missing prompt links:")
        for path in missing:
            print(f"- {path}")
        return 1

    print("README.md indexes every prompt.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
