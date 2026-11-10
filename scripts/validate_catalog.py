#!/usr/bin/env python3
"""Validate catalog structure and its generated README projection.

The catalog uses JSON syntax because JSON is a strict subset of YAML 1.2. This
keeps local and CI validation dependency-free while retaining a .yaml source.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "languages.yaml"
README = ROOT / "README.md"

CATEGORIES = {
    "agent-first",
    "llm-prompt",
    "agent-workflow",
    "verified-agent-safe",
    "probabilistic",
    "ai-compute",
    "experimental-research",
    "adjacent-tooling",
}
CLASSIFICATIONS = {
    "standalone-language",
    "embedded-dsl",
    "framework",
    "programming-model",
}
REQUIRED = {
    "id", "name", "aliases", "repository_url", "documentation_url",
    "description", "primary_category", "secondary_tags", "classification",
    "ai_capabilities", "execution_model", "license", "maturity", "archived",
    "last_verified", "evidence_urls",
}
ENTRY_RE = re.compile(r"^- \[(?P<name>[^]]+)]\((?P<url>https?://[^)]+)\) - (?P<description>.+)\.$")
START = "<!-- catalog:start -->"
END = "<!-- catalog:end -->"


def valid_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def main() -> int:
    errors: list[str] = []
    try:
        data = json.loads(CATALOG.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"catalog: cannot load {CATALOG}: {exc}", file=sys.stderr)
        return 1

    projects = data.get("projects")
    if not isinstance(projects, list):
        print("catalog: projects must be an array", file=sys.stderr)
        return 1

    seen: dict[str, Counter[str]] = {
        "id": Counter(), "name": Counter(), "repository_url": Counter()
    }
    by_category: dict[str, list[str]] = defaultdict(list)

    for index, project in enumerate(projects):
        label = f"projects[{index}]"
        if not isinstance(project, dict):
            errors.append(f"{label}: must be an object")
            continue
        missing = REQUIRED - project.keys()
        extra = project.keys() - REQUIRED
        if missing:
            errors.append(f"{label}: missing fields: {', '.join(sorted(missing))}")
        if extra:
            errors.append(f"{label}: unexpected fields: {', '.join(sorted(extra))}")
        for field in ("id", "name"):
            value = project.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{label}.{field}: must be a non-empty string")
            else:
                seen[field][value.casefold()] += 1
        repo = project.get("repository_url")
        docs = project.get("documentation_url")
        if repo is not None:
            if not valid_url(repo):
                errors.append(f"{label}.repository_url: malformed URL")
            else:
                seen["repository_url"][repo.rstrip("/").casefold()] += 1
        if repo is None and docs is None:
            errors.append(f"{label}: repository_url and documentation_url cannot both be null")
        if docs is not None and not valid_url(docs):
            errors.append(f"{label}.documentation_url: malformed URL")
        category = project.get("primary_category")
        if category not in CATEGORIES:
            errors.append(f"{label}.primary_category: invalid category {category!r}")
        else:
            by_category[category].append(project.get("name", ""))
        if project.get("classification") not in CLASSIFICATIONS:
            errors.append(f"{label}.classification: invalid classification")
        if not isinstance(project.get("archived"), bool):
            errors.append(f"{label}.archived: must be boolean")
        for field in ("aliases", "secondary_tags", "ai_capabilities", "evidence_urls"):
            value = project.get(field)
            if not isinstance(value, list):
                errors.append(f"{label}.{field}: must be an array")
            elif len(value) != len(set(value)):
                errors.append(f"{label}.{field}: contains duplicates")
        if not project.get("ai_capabilities"):
            errors.append(f"{label}.ai_capabilities: must not be empty")
        evidence = project.get("evidence_urls", [])
        if isinstance(evidence, list):
            for url in evidence:
                if not valid_url(url):
                    errors.append(f"{label}.evidence_urls: malformed URL {url!r}")
            primary = repo or docs
            if primary and primary not in evidence:
                errors.append(f"{label}.evidence_urls: must contain the primary link")
        try:
            date.fromisoformat(project.get("last_verified", ""))
        except (TypeError, ValueError):
            errors.append(f"{label}.last_verified: must be an ISO date")
        description = project.get("description")
        if not isinstance(description, str) or len(description) < 20:
            errors.append(f"{label}.description: must be at least 20 characters")

    for field, counts in seen.items():
        for value, count in counts.items():
            if count > 1:
                errors.append(f"duplicate {field}: {value!r} appears {count} times")

    for category, names in by_category.items():
        expected = sorted(names, key=str.casefold)
        if names != expected:
            errors.append(f"category {category!r} is not alphabetized")

    try:
        readme = README.read_text(encoding="utf-8")
        projection = readme.split(START, 1)[1].split(END, 1)[0]
    except (OSError, IndexError) as exc:
        errors.append(f"README catalog markers are missing or unreadable: {exc}")
        projection = ""

    readme_entries: dict[str, tuple[str, str]] = {}
    for line in projection.splitlines():
        if not line.startswith("- ["):
            continue
        match = ENTRY_RE.match(line)
        if not match:
            errors.append(f"README entry has invalid format: {line}")
            continue
        name = match.group("name")
        if name in readme_entries:
            errors.append(f"README contains duplicate entry: {name}")
        readme_entries[name] = (match.group("url"), match.group("description"))

    catalog_entries = {
        project["name"]: (project["repository_url"] or project["documentation_url"], project["description"])
        for project in projects if isinstance(project, dict) and project.get("name")
    }
    for name in sorted(catalog_entries.keys() - readme_entries.keys(), key=str.casefold):
        errors.append(f"README is missing catalog project: {name}")
    for name in sorted(readme_entries.keys() - catalog_entries.keys(), key=str.casefold):
        errors.append(f"README project is absent from catalog: {name}")
    for name in catalog_entries.keys() & readme_entries.keys():
        if catalog_entries[name] != readme_entries[name]:
            errors.append(f"README metadata differs from catalog: {name}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(f"Catalog valid: {len(projects)} projects across {len(by_category)} categories.")
    for category in sorted(by_category):
        print(f"  {category}: {len(by_category[category])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
