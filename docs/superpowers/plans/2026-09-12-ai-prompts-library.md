# AI Prompts Library Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish a public, indexed repository containing the two supplied reusable prompts.

**Architecture:** Store prompts as standalone Markdown files and maintain a human-written README catalog. A small Python checker and GitHub Actions workflow enforce that every prompt is linked from the catalog.

**Tech Stack:** Markdown, Python 3 standard library, GitHub Actions, Git/GitHub CLI

**Spec:** `docs/superpowers/specs/2026-09-12-ai-prompts-library-design.md`

## Global Constraints

- The GitHub repository is public.
- Initial prompt content is copied without substantive alteration.
- Every Markdown file directly under `prompts/` is linked from `README.md` with a basic-purpose description.
- The checker has no third-party dependencies.

---

### Task 1: README index checker

**Files:**
- Create: `tests/test_check_readme_index.py`
- Create: `scripts/check_readme_index.py`

**Interfaces:**
- Consumes: a repository root containing `README.md` and `prompts/*.md`
- Produces: `missing_prompt_links(root: Path) -> list[str]` and CLI exit code `0` when complete, `1` when entries are missing

- [ ] Write unit tests proving a complete index passes and a missing prompt link is reported.
- [ ] Run `python -m unittest discover -s tests -v` and confirm failure because the checker module does not exist.
- [ ] Implement the minimum checker.
- [ ] Re-run the unit tests and confirm they pass.

### Task 2: Prompt catalog and automation

**Files:**
- Create: `prompts/academic-paper-summary.md`
- Create: `prompts/anki-apkg-continuous-learning.md`
- Create: `README.md`
- Create: `.github/workflows/validate-readme.yml`
- Create: `LICENSE`

**Interfaces:**
- Consumes: the two supplied source Markdown files
- Produces: a browsable README catalog and CI validation on pushes and pull requests

- [ ] Copy both source prompts into stable repository paths without substantive changes.
- [ ] Add both prompt links and concise purpose descriptions to `README.md`.
- [ ] Add a GitHub Actions workflow that runs unit tests and the repository checker.
- [ ] Run `python -m unittest discover -s tests -v` and `python scripts/check_readme_index.py`.

### Task 3: Publish

**Files:**
- Modify: Git metadata and GitHub repository state

**Interfaces:**
- Consumes: verified local repository on branch `main`
- Produces: public GitHub repository `FZ010619/ai-prompts-library`

- [ ] Commit all repository files on `main`.
- [ ] Create the public GitHub repository and push `main`.
- [ ] Verify remote URL, clean working tree, default branch, and public visibility.

