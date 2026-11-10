# Taxonomy

The catalog assigns each project one primary category based on the capability that most strongly defines its language design. Secondary features do not create duplicate entries.

## Category boundaries

### Agent-First and AI-Native General-Purpose Languages

Languages whose intended author is an AI agent or whose general-purpose syntax and tooling are explicitly designed for machine authorship. A conventional language with an optional coding assistant does not qualify.

### LLM and Prompt Programming Languages

Languages and embedded DSLs where model invocation, prompt composition, constrained decoding, or structured model output is a central semantic concern. Model-serving infrastructure alone is insufficient unless it also exposes a language-like programming surface.

### Agent Orchestration and Workflow Languages

Languages and programming models that make tools, agent calls, state, approval, capabilities, or workflow coordination explicit. A framework with only conventional host-language APIs normally belongs in adjacent tooling.

### Verified, Contract-Driven, and Agent-Safe Languages

Languages where contracts, proofs, types, effects, capabilities, or structured editing are central safeguards for agent-authored code. This category requires native language or compiler behavior, not a testing library added through ordinary integration.

### Probabilistic Programming Languages

Languages where random choice, conditioning, model specification, and automated or programmable inference are fundamental semantics.

### Differentiable and AI-Compute Languages

Languages primarily organized around automatic differentiation, arrays, tensor kernels, GPUs, or heterogeneous accelerators. Mojo belongs here because its defining AI contribution is compute; it is not an LLM orchestration language.

### Experimental and Research Languages

Academic artifacts, thought experiments, early prototypes, and unusual models with enough primary evidence to study but limited evidence of production use or stability.

### Adjacent Frameworks and Agent Tooling

Influential agent runtimes and AI programming frameworks that do not define a standalone language. Goose is an agent and DSPy is a Python framework; keeping them here prevents the main catalog from conflating tools with languages.

## Classification field

- `standalone-language`: owns its syntax and compiler or interpreter.
- `embedded-dsl`: uses a host language while adding a distinct language-like surface.
- `programming-model`: defines executable structure or semantics without a conventional standalone syntax.
- `framework`: supplies APIs and runtime behavior in an existing language.

## Capability evidence

The comparison guide distinguishes native features from integrations:

- **Native** means syntax, static semantics, compiler behavior, or a required runtime construct implements the capability.
- **Integrated** means the project exposes the capability through an official host-language library or adapter.
- **Unknown** means available primary evidence does not establish support.

Roadmap items, third-party plugins, and plausible implementation techniques do not count as supported capabilities.
