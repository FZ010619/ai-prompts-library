# AI Prompts Library Design

## Goal

Create a public GitHub repository for reusable Chinese AI prompts, starting with two supplied Markdown files. The repository must make each prompt's purpose easy to discover and prevent new prompt files from being added without a matching README entry.

## Repository structure

- `prompts/` contains one Markdown file per reusable prompt.
- `README.md` contains a table with each prompt's name, basic purpose, and relative link.
- `scripts/check_readme_index.py` verifies that every Markdown file directly under `prompts/` is linked from `README.md`.
- `tests/` contains standard-library unit tests for the checker.
- `.github/workflows/validate-readme.yml` runs the tests and checker on pushes and pull requests.
- `LICENSE` uses the MIT license.

## Initial prompts

1. `academic-paper-summary.md` preserves the supplied prompt for concise mining-subsidence paper summaries.
2. `anki-apkg-continuous-learning.md` preserves the supplied prompt for maintaining comprehensive Anki APKG decks.

The repository uses stable ASCII filenames for compatibility while keeping the Chinese title and original content inside each document.

## README maintenance rule

Every new file added directly under `prompts/` must also be linked from the README prompt table with a short purpose description. CI fails when a prompt is missing from the README, making the maintenance rule visible and enforceable.

## Verification

- Unit tests cover a fully indexed repository and a missing README entry.
- The repository-level checker must pass against the committed files.
- Git status, configured remote, and GitHub repository visibility are checked after pushing.

