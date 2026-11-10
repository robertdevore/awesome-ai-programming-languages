# Contributing

Thank you for helping improve Awesome AI Programming Languages.

## Before proposing a project

Read [the inclusion criteria](docs/inclusion-criteria.md) and [taxonomy](docs/taxonomy.md). A project must have a language-like surface and primary evidence sufficient to verify its purpose, status, and classification. General-purpose agent frameworks belong only in the adjacent section.

Search the README, catalog, open issues, and pull requests for the project and its aliases before opening a proposal.

## Project proposals

Use the **New language** issue template or submit a pull request that:

1. Adds one record to `data/languages.yaml` in the correct category and alphabetical position.
2. Adds the matching one-line README entry in the generated catalog block.
3. Uses the canonical project repository and primary documentation.
4. Supplies evidence URLs for every capability, license, maturity, and status claim.
5. Updates `docs/comparison.md` only when the project is significant enough for the major-project matrix.
6. Runs `python3 scripts/validate_catalog.py` successfully.

Use `null` for facts that cannot be established. Do not infer a license from package metadata or a repository description when no authoritative license is published.

## Corrections

Use the **Correction** issue template. Include the current text, proposed text, primary source, and date checked. Project maintainers are welcome to correct factual errors, but inclusion and category decisions remain editorial.

## Editorial style

- Use `- [Project](canonical-url) - Neutral one-sentence description.`
- Start descriptions with an article or clear noun phrase.
- Avoid rankings, endorsements, star counts, unsupported benchmarks, and marketing adjectives.
- Describe shipped behavior, not roadmap claims, unless the roadmap status is explicit.
- Keep one primary category per project; use tags and comparison notes for secondary capabilities.
- Alphabetize entries by displayed project name within each category.

## Pull requests

Keep each pull request focused. Complete the pull request checklist and explain any unknown metadata or ambiguous classification. Maintainers may request stronger evidence, narrower claims, or placement in research notes instead of the main list.

By contributing repository-authored list content, you agree that it is released under [CC0 1.0 Universal](LICENSE). Linked projects retain their own licenses.
