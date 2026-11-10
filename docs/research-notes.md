# Research Notes

Last reviewed: **2026-11-10**.

These notes preserve the discovery trail, candidate dispositions, and unresolved questions without overloading the README. Repository and documentation claims were checked against official GitHub metadata, official project sites, or primary papers. The [agentlanguages.dev catalog](https://agentlanguages.dev/) was used for discovery and classification leads, not as the sole authority for inclusion.

## Baseline sources reviewed

- [sindresorhus/awesome](https://github.com/sindresorhus/awesome) for list conventions, scope discipline, and CC0 precedent.
- [Awesome AI-Driven Development](https://github.com/eltociear/awesome-AI-driven-development) for adjacent-tool discovery.
- [Awesome Programming Languages](https://github.com/ChessMax/awesome-programming-languages) and [linsa-io/programming-languages](https://github.com/linsa-io/programming-languages) for language-list structure.
- [agentlanguages.dev](https://agentlanguages.dev/) for emerging agent-authored language discovery.
- [Probabilistic-Programming.org](https://probabilistic-programming.org/) plus each project's official repository for probabilistic-language coverage.
- Official repositories and documentation linked from each record in [`data/languages.yaml`](../data/languages.yaml).
- Primary papers for [Pel](https://arxiv.org/abs/2505.13453) and [Quasar](https://mell.ac/projects/quasar/).

## Seed-set disposition

### Included

The following candidates were verified and included, though some moved to a category different from the discovery report when primary evidence supported a clearer classification:

- **Agent-native and general-purpose:** AILANG, BAML, Bend 2, Fluxon, Kujo, MoonBit, NERD, Vera, and Zero/Zerolang.
- **Prompt and LLM:** APPL, Colang, Guidance, LMQL, Prompt Declaration Language, Prompt Programming Language, and SGLang. DSPy is included in adjacent tooling because its official description identifies it as a Python framework.
- **Probabilistic:** Anglican, Gen, NumPyro, Pyro, Stan, Turing.jl, and WebPPL.
- **AI compute:** Dex, Mojo, and Triton.
- **Agent/workflow:** AgentDSL, AWFL, Boruna, Fabro, Lumen, Marsha, Pel, Plasm, and Quasar.
- **Adjacent tooling:** AutoGen, DSPy, Goose, LangGraph, LlamaIndex Workflows, PydanticAI, and Semantic Kernel.
- **Additional research candidates:** Aria, Aver, Axis, B-IR/Loom, Canlang, Codong, Cohesive, Faber Romanus, Gooo, Hale, ilo, Intent, Jacquard, Laze, LLMLang, Lom, Lume, Magpie, Modula-9, Mog, Muro, NanoLang, Pact, Prajna, reqlan, SEMAPRAX, Sentience, Sever, Sigil, Tacit, Thermite, Vow, With, and X07.

Each included project has one catalog record and one README entry. Projects that span camps are assigned to the category that best matches their defining shipped behavior.

### Deferred or excluded

| Candidate | Disposition | Reason |
| --- | --- | --- |
| KERN | Deferred | Searches of GitHub and the supplied discovery sources did not identify a canonical AI-language repository or primary project page with enough evidence to disambiguate the name. |
| linkly | Deferred | No canonical language project could be resolved from the name; search results were unrelated applications and libraries. |
| Prove | Deferred | An official project site describes a working compiler, but no canonical public source repository was exposed during review and its custom source license needs owner review before main-list treatment. |

No candidate was excluded merely for low stars, recent creation, or research status.

## Classification decisions

- **BAML** is placed under LLM and prompt programming because typed LLM functions and structured outputs are its central language surface.
- **Bend 2, Vera, and Zero** are placed under verified and agent-safe languages because proof or contract checking is the defining differentiator.
- **MoonBit** is listed under agent-safe languages because it is a general-purpose language with a structured compiler toolchain and official agent guidance; it is not presented as an LLM orchestration language.
- **Mojo** is an AI-compute language because its defining focus is heterogeneous systems and accelerator programming.
- **SGLang** remains in the prompt-language category because its official frontend exposes a language-like structured generation model, even though the project also provides model serving.
- **Goose** is an agent, **DSPy** is a framework, and the remaining adjacent entries are host-language runtimes; none is represented as a standalone programming language.
- **Lume** and **Lumen** are distinct projects: Lume is a Go-transpiled backend language; Lumen is a Markdown-native workflow language.
- **Pact** refers specifically to `KikotVit/pact-lang`, not Kadena's unrelated smart-contract language.
- **B-IR / Loom** is treated as one experiment because the project documents successive iterations of the same investigation.

## Known metadata gaps

The catalog intentionally records `null` where the reviewed primary source did not establish a value. Important gaps include unpublished or unclear licenses for several emerging languages, Pel's lack of a canonical public repository, and MoonBit's documentation repository serving as the canonical public source link rather than a compiler repository.

## External-link verification

Canonical GitHub repositories were checked through the GitHub API where available. Official sites were reviewed directly. The Codong project site failed TLS certificate validation on 2026-11-10, so the catalog retains only its reachable canonical repository until the site is repaired. Other documentation hosts may reject automated `HEAD` requests or rate-limit link checkers; such failures are inconclusive and should be recorded rather than converted into automatic removals.

## Unresolved research questions

1. Can KERN and linkly be tied to canonical primary artifacts with verifiable authorship?
2. Will Prove publish a canonical source repository, and how should its split custom/tooling licenses be represented?
3. Should MoonBit expose an official compiler source repository suitable for the catalog's canonical repository field?
4. Which early 2026 agent-language projects will continue active development long enough to move out of the experimental section?

## Recommended checks before public launch

1. Obtain owner approval for CC0 dedication and the breadth of the experimental section.
2. Re-run live external-link and GitHub archival checks immediately before publication.
3. Resolve or prominently retain every unknown license; do not imply that an unlicensed project is open source.
4. Ask maintainers of ambiguous or very new projects to confirm canonical URLs and neutral descriptions.
5. Review the comparison matrix with project maintainers where practical, especially native-versus-integrated capability markings.
6. Keep the repository private until the owner explicitly approves publication.
