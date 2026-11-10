# Awesome AI Programming Languages

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Built by Kujo](https://img.shields.io/badge/built%20by-Kujo-black.svg)](https://github.com/kujolang/kujo)

A curated list of programming languages, domain-specific languages, and programming models for AI-native software development. Projects are grouped by purpose and language type so developers can compare systems that address similar needs.

This is an independent editorial resource, not an endorsement of any listed project. Project descriptions summarize verified official material and avoid ranking, star counts, and unverified performance claims.

## Scope

A project belongs in the main language categories when it provides a distinct syntax, semantics, compiler/interpreter, or language-like programming model for AI authorship, model interaction, agent coordination, verification, probabilistic inference, or AI compute. Mature systems and useful research prototypes are both eligible when primary evidence is available. General AI tools belong only in the clearly separated adjacent section.

See [Inclusion Criteria](docs/inclusion-criteria.md) for the complete review standard. Structured metadata, evidence links, licenses, maturity, and verification dates live in [`data/languages.yaml`](data/languages.yaml). Unknown values are recorded as `null` rather than inferred.

## Contents

- [Agent-First and AI-Native General-Purpose Languages](#agent-first-and-ai-native-general-purpose-languages)
- [LLM and Prompt Programming Languages](#llm-and-prompt-programming-languages)
- [Agent Orchestration and Workflow Languages](#agent-orchestration-and-workflow-languages)
- [Verified, Contract-Driven, and Agent-Safe Languages](#verified-contract-driven-and-agent-safe-languages)
- [Probabilistic Programming Languages](#probabilistic-programming-languages)
- [Differentiable and AI-Compute Languages](#differentiable-and-ai-compute-languages)
- [Experimental and Research Languages](#experimental-and-research-languages)
- [Adjacent Frameworks and Agent Tooling](#adjacent-frameworks-and-agent-tooling)
- [Comparison Guide](docs/comparison.md)
- [Taxonomy](docs/taxonomy.md)
- [Research Notes](docs/research-notes.md)
- [Contributing](#contributing)
- [License](#license)

<!-- catalog:start -->
## Agent-First and AI-Native General-Purpose Languages

Languages designed for AI agents to write, maintain, execute, or reason about software.

- [AILANG](https://github.com/sunholo-data/ailang) - A deterministic language with explicit effects and an AI-oriented toolchain for agent-authored programs.
- [Codong](https://github.com/brettinhere/Codong) - A Go-transpiled language that limits common tasks to canonical forms intended to reduce agent choice.
- [Faber Romanus](https://github.com/faberlang/faber) - A compact, statically typed language designed for machine authorship and native compilation.
- [Fluxon](https://github.com/fluxon-lang/fluxon) - A token-conscious general-purpose language with canonical syntax and agent-oriented tooling.
- [ilo](https://github.com/ilo-lang/ilo) - A small compiled language whose regular syntax and structured diagnostics target LLM authors.
- [Kujo](https://github.com/kujolang/kujo) - A general-purpose language and toolchain for building AI-native software with agent-oriented development workflows.
- [Lume](https://github.com/mavboas/lume) - An immutable-by-default backend language that transpiles to Go and includes token-budgeted context tooling.
- [Magpie](https://github.com/magpie-lang/magpie) - A machine-oriented language that exposes static single-assignment form as its source syntax.
- [Mog](https://github.com/voltropy/mog) - A compact statically typed language with flat operators and host-granted capabilities.
- [NERD](https://github.com/Nerd-Lang/nerd-lang-core) - An intermediate language for machine authorship with English keywords, structured diagnostics, and model and MCP primitives.
- [Tacit](https://github.com/weetster/tacit) - A compiled language with a constrained, regular surface intended for reliable LLM generation.
- [With](https://github.com/withlang-dev/with) - A typed language designed around explicit context and predictable agent-generated code.
- [X07](https://github.com/x07lang/x07) - A language whose canonical JSON AST and patch-based edits support structured program generation by agents.

## LLM and Prompt Programming Languages

Languages and DSLs for model invocation, structured generation, prompting, constraints, and typed model interactions.

- [APPL](https://github.com/appl-team/appl) - A Python-embedded prompt programming language that composes model calls with ordinary program logic.
- [BAML](https://github.com/BoundaryML/baml) - A language for typed LLM functions that generates client code and parses structured model outputs.
- [Colang](https://github.com/NVIDIA-NeMo/Guardrails) - A conversational DSL in NeMo Guardrails for specifying dialogue flows and model guardrails.
- [Guidance](https://github.com/guidance-ai/guidance) - A Python-embedded language for constrained generation, control flow, and structured model outputs.
- [LMQL](https://github.com/eth-sri/lmql) - A query language for language models with constraints, control flow, and decoding directives.
- [Prompt Declaration Language](https://github.com/IBM/prompt-declaration-language) - A YAML-based declarative language for composing prompts, model calls, tools, and traditional control flow.
- [Prompt Programming Language](https://github.com/williambrendel/Prompt-Programming-Language) - A structured, indentation-based DSL for organizing prompts, variables, and refinement steps.
- [SGLang](https://github.com/sgl-project/sglang) - A language and serving system for structured LLM programs, including model calls, control flow, and constrained outputs.

## Agent Orchestration and Workflow Languages

Languages with constructs for agent execution, tools, workflows, state, capabilities, approvals, and coordination.

- [AgentDSL](https://github.com/nathaniel-gordon/agentdsl) - A typed DSL and compiler pipeline for asynchronous agent workflows.
- [AWFL](https://github.com/awfl-us/dsl) - A typed Scala DSL for composing and executing agent workflows.
- [Boruna](https://github.com/escapeboy/boruna) - A deterministic workflow language with declared effects, capability policies, and tamper-evident execution evidence.
- [Fabro](https://github.com/fabro-sh/fabro) - A declarative workflow system for coordinating coding agents through reviewable software-development pipelines.
- [Lumen](https://github.com/alliecatowo/lumen) - A Markdown-native, statically typed language for deterministic AI workflows and provider calls.
- [Marsha](https://github.com/alantech/marsha) - A functional English-like language that uses an LLM-backed compiler to produce tested Python programs.
- [Pel](https://arxiv.org/abs/2505.13453) - A research language for capability-controlled inter-agent communication and automatically parallelized orchestration.
- [Plasm](https://github.com/PlasmTools/plasm-core) - A typed capability-graph and mapping language for describing agent access to external APIs.
- [Quasar](https://github.com/stephenmell/quasar-colm2026-artifact) - A research language for LLM code actions with effect separation, approval batching, parallel execution, and conformal semantics.

## Verified, Contract-Driven, and Agent-Safe Languages

Languages centered on correctness, formal verification, machine-checkable contracts, structured editing, or safer execution.

- [Aver](https://github.com/jasisz/aver) - A contract-oriented language designed to make agent-authored behavior mechanically checkable.
- [Bend 2](https://github.com/bendlang/bend) - A proof-oriented language that checks program properties intended to prevent common AI-generated mistakes.
- [BHC/hx](https://github.com/arcanist-sh/hx) - An experimental verified language stack combining an agent-facing syntax with a capability-aware compiler.
- [Cohesive](https://github.com/cohesivesystems/cohesive) - A specification- and contract-oriented language for producing checkable agent-authored programs.
- [Hale](https://github.com/hale-lang/hale) - A typed language that emphasizes explicit effects and compiler-enforced constraints for machine-generated code.
- [Intent](https://github.com/lhaig/intent) - An intent- and contract-oriented language for compiling high-level specifications into checked programs.
- [Jacquard](https://github.com/jbwinters/jacquard-lang) - A language with explicit contracts and structured diagnostics for reliable machine authorship.
- [Lom](https://github.com/lom-lang/lom) - A statically checked language designed to constrain and verify programs generated by language models.
- [Modula-9](https://github.com/atverm/m9c) - A contract-focused systems language with an agent-oriented compiler and tutorial.
- [MoonBit](https://github.com/moonbitlang/moonbit-docs) - A general-purpose language and WebAssembly toolchain with structured tooling and dedicated guidance for coding agents.
- [Muro](https://github.com/murolang/muro) - An experimental contract-driven language for constrained machine authorship.
- [NanoLang](https://github.com/jordanhubbard/nanolang) - A compact, statically checked language designed for reliable generation within small model contexts.
- [Pact](https://github.com/KikotVit/pact-lang) - A contract-based language for agent-generated programs with compiler-checked obligations.
- [reqlan](https://github.com/littletuna4/reqlan) - A requirements-oriented language that connects executable specifications to generated implementations.
- [SEMAPRAX](https://github.com/wavect/semaprax) - A semantically explicit language with machine-checkable contracts for agent-authored software.
- [Sigil](https://github.com/goodnasubi/sigil) - A typed, verification-oriented language for predictable AI-generated programs.
- [Thermite](https://github.com/dollspace-gay/Thermite) - A verification-oriented compiled language with contracts for machine-authored code.
- [Vera](https://github.com/aallan/vera) - A language with mandatory function contracts, SMT-backed verification, typed slots, and first-class model inference.
- [Vow](https://github.com/vow-lang/vow) - A contract-first language that turns specifications into compiler-checkable obligations for agent-authored code.
- [Zero](https://github.com/vercel-labs/zerolang) - An early agent-oriented language centered on typed specifications and mechanically checked implementations.

## Probabilistic Programming Languages

Languages where stochastic computation, conditioning, and probabilistic inference are fundamental.

- [Anglican](https://github.com/probprog/anglican) - A Clojure-hosted probabilistic programming system for composing models and inference algorithms.
- [Gen](https://github.com/probcomp/Gen.jl) - A Julia probabilistic programming system with programmable inference.
- [NumPyro](https://github.com/pyro-ppl/numpyro) - A JAX-based probabilistic programming library with automatic differentiation and accelerator execution.
- [Pyro](https://github.com/pyro-ppl/pyro) - A universal probabilistic programming language embedded in Python and backed by PyTorch.
- [Stan](https://github.com/stan-dev/stan) - A standalone probabilistic language for Bayesian statistical modeling and inference.
- [Turing.jl](https://github.com/TuringLang/Turing.jl) - A Julia probabilistic programming system for Bayesian modeling and composable inference.
- [WebPPL](https://github.com/probmods/webppl) - A JavaScript-like probabilistic programming language for teaching and research.

## Differentiable and AI-Compute Languages

Languages designed around differentiation, tensor computation, GPUs, accelerators, or machine-learning execution.

- [Dex](https://github.com/google-research/dex-lang) - A research language for typed array programming and differentiable functions.
- [Mojo](https://github.com/modular/modular) - A systems programming language for heterogeneous AI compute with Python interoperability.
- [Triton](https://github.com/triton-lang/triton) - A Python-embedded language and compiler for writing efficient custom GPU kernels.

## Experimental and Research Languages

Early prototypes, academic systems, thought experiments, and unusual emerging programming models.

- [Aria](https://github.com/dan-strohschein/aria) - An experimental self-hosting language developed for AI-first programming workflows.
- [Axis](https://github.com/vmelnic/axis) - An LL(1) backend language for small models with constrained-decoding masks and generated service artifacts.
- [B-IR / Loom](https://github.com/imjasonh/loom) - A documented experiment in machine-oriented intermediate languages that evolved toward explicit contracts and stable errors.
- [Canlang](https://github.com/veighnsche/canlang) - An experimental business-application language that derives forms and agent tools from checked operations.
- [Gooo](https://github.com/kimjooyoon/meta-ontology-go) - An experimental ontology-oriented language and compiler intended for machine-authored software.
- [Laze](https://github.com/kerv/laze) - A small experimental language exploring syntax optimized for model generation.
- [LLMLang](https://github.com/paulprogrammer/llmlang) - A dense prefix language with indexed variables, structured diagnostics, and an MCP editing surface.
- [Prajna](https://github.com/joyboseroy/prajna) - A small research prototype exploring a minimal AI-native language implementation.
- [Sentience](https://github.com/nbursa/sentience) - An experimental language organized around contextual agents and persistent memory.
- [Sever](https://github.com/AvitalTamir/sever) - A thought experiment in asking a model to design a language for machine rather than human authors.

## Adjacent Frameworks and Agent Tooling

Influential frameworks and runtimes that shape AI-native programming but are not themselves standalone programming languages.

- [AutoGen](https://github.com/microsoft/autogen) - A framework for building event-driven single- and multi-agent applications.
- [DSPy](https://github.com/stanfordnlp/dspy) - A Python framework for defining and optimizing modular programs that call language models.
- [Goose](https://github.com/aaif-goose/goose) - An extensible coding agent that can plan, edit, execute, and test with pluggable models and tools.
- [LangGraph](https://github.com/langchain-ai/langgraph) - A graph-based runtime for stateful, long-running agent workflows.
- [LlamaIndex Workflows](https://github.com/run-llama/llama-agents) - An event-driven, async-first framework for controlling agent and application execution flows.
- [PydanticAI](https://github.com/pydantic/pydantic-ai) - A typed Python agent framework built around Pydantic validation and model-agnostic interfaces.
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel) - An SDK for composing model calls, plugins, memory, and agent workflows in conventional languages.

<!-- catalog:end -->

## Comparison Guide

Use the [comparison guide](docs/comparison.md) to compare major projects across language form, model calls, workflow constructs, structured outputs, verification, capability controls, accelerator support, execution model, and maturity. A check mark appears only where official evidence establishes a native capability.

## Taxonomy

The [taxonomy](docs/taxonomy.md) explains category boundaries, primary-category assignment, and the distinction between native language features and library integrations.

## Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) and the [inclusion criteria](docs/inclusion-criteria.md) before proposing a project or correction. Every factual change should include primary evidence.

## License

The curated list and repository-authored documentation are dedicated to the public domain under [CC0 1.0 Universal](LICENSE). Linked projects retain their own licenses.
