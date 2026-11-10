# AGENTS.md

## Purpose

Maintain this repository as a neutral, evidence-based Awesome list of AI-native programming languages, DSLs, programming models, and clearly separated adjacent tooling.

## Source of truth

- `data/languages.yaml` is canonical metadata. It uses JSON syntax, which is valid YAML 1.2, so validation stays dependency-free.
- Every catalog project must appear exactly once in the README block between `<!-- catalog:start -->` and `<!-- catalog:end -->`.
- `data/schema.json` documents the catalog contract.
- `docs/research-notes.md` records considered but deferred or excluded candidates.

## Editing rules

1. Verify claims from an official repository, official documentation, or a primary paper.
2. Give each project one primary category. Record overlap through tags or comparison notes; never duplicate an entry.
3. Use `null` for unknown facts. Do not infer a license, maturity, or capability.
4. Keep entries alphabetical within categories and descriptions neutral.
5. Treat frameworks as adjacent tooling unless they define a genuine language or DSL.
6. Preserve Kujo's neutral treatment; do not promote it or any other project disproportionately.
7. Update `last_verified` and evidence URLs when changing facts.
8. Do not enable Pages, publish a website, install GitHub Apps, or change repository visibility without owner approval.

## Required checks

Run:

```sh
python3 scripts/validate_catalog.py
```

Also inspect changed Markdown links and anchors. External link checks may fail because of rate limits or bot protection; report those separately rather than deleting an otherwise authoritative source.

## Pull requests

Work on a branch, use focused commits, and open a pull request to `main`. Do not merge without owner approval.
