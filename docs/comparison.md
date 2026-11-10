# Comparison Guide

This matrix is a navigation aid, not a ranking. It compares representative projects from each category. Consult the canonical catalog record and official evidence before choosing a project.

**Legend:** **N** = native language or compiler capability; **E** = official embedded DSL or framework capability; **T** = official agent-facing tooling rather than language semantics; **—** = not established by the reviewed primary evidence. “Maturity” is the catalog's editorial status, not a quality score.

| Project | Form | Agent authorship | First-class model calls | Native workflow constructs | Typed structured outputs | Contracts / verification | Capabilities / approvals | GPU / accelerator | Execution | Maturity |
| --- | --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | --- | --- |
| AILANG | Standalone | N | — | — | — | N | N | — | Compiler + VM | Working compiler |
| APPL | Embedded in Python | — | E | E | — | — | — | — | Python runtime | Active |
| BAML | Standalone DSL | — | N | — | N | N | — | — | Compiler + generated clients | Active |
| Bend 2 | Standalone | N | — | — | — | N | — | — | Compiler + prover | Active |
| Boruna | Standalone | N | N | N | N | N | N | — | Custom VM | Working compiler |
| Colang | Embedded DSL | — | E | E | — | E | E | — | NeMo Guardrails runtime | Active |
| Guidance | Embedded in Python | — | E | E | E | — | — | — | Python runtime | Active |
| Kujo | Standalone | N | N | N | N | T | N | — | Compiler + runtime | Active development |
| LMQL | Standalone DSL | — | N | N | N | N | — | — | Compiler + runtime | Active |
| Lumen | Standalone | N | N | N | N | N | N | — | Interpreter | Working compiler |
| Mojo | Standalone | — | — | — | — | N | — | N | Compiler + runtime | Active |
| MoonBit | Standalone | T | — | — | — | N | — | — | Compiler + toolchain | Production |
| NERD | Standalone | N | N | N | — | T | N | — | LLVM compiler | Working compiler |
| PDL | YAML DSL | — | N | N | N | N | E | — | Interpreter | Active |
| Pel | Standalone research language | N | N | N | — | N | N | — | Research interpreter | Research prototype |
| Pyro | Embedded in Python | — | — | — | — | — | — | E | Python + PyTorch | Active |
| Quasar | Standalone research language | N | N | N | — | N | N | — | Transpiler + interpreter | Research artifact |
| SGLang | Embedded in Python | — | E | E | E | — | — | E | Frontend + serving runtime | Production |
| Stan | Standalone | — | — | — | — | N | — | — | Compiler + inference runtime | Mature |
| Triton | Embedded in Python | — | — | — | — | N | — | N | GPU compiler | Production |
| Vera | Standalone | N | N | — | N | N | N | — | WebAssembly compiler | Working compiler |
| X07 | Standalone | N | — | — | — | N | N | — | Compiler + interpreter | Working compiler |

## Framework boundary examples

The adjacent projects expose important programming abstractions through host-language APIs, not new standalone languages:

| Project | Host surface | Structured outputs | Agent / workflow model | Validation or safety |
| --- | --- | :---: | :---: | :---: |
| AutoGen | Python / .NET APIs | E | E | E |
| DSPy | Python modules and optimizers | E | E | E |
| Goose | Agent configuration and tools | E | E | E |
| LangGraph | Python / JavaScript graph APIs | E | E | E |
| LlamaIndex Workflows | Python event and step APIs | E | E | E |
| PydanticAI | Typed Python APIs | E | E | E |
| Semantic Kernel | .NET / Python / Java APIs | E | E | E |

## Reading the matrix

- A language can be useful for AI without calling an LLM at runtime. Bend 2 and X07 target safer machine authorship; Mojo and Triton target AI computation.
- A type system alone does not imply formal verification. The verification column is marked only for documented contracts, proof obligations, static constraints, or comparable compiler checks relevant to the listed capability.
- Framework rows use **E** because their features are host-language integrations. They should not be compared as though they were standalone syntax or semantics.
- Blank capability cells are conservative. They do not prove that a project cannot support the feature through libraries or future releases.

Primary evidence is recorded in [`data/languages.yaml`](../data/languages.yaml); classification rules are in [the taxonomy](taxonomy.md).
