# Gobstraction

Gobstraction is a small set of agent skills for architecture decisions where the agent is allowed to choose the structure rather than merely implement a prescribed one.

Its premise is simple: existing abstractions are evidence, not authority. Recover the real requirements, invariants, variation, and composition constraints first; then keep the smallest structure that represents them faithfully.

## Skills

| Skill | Use it for |
| --- | --- |
| `gobstraction` | Default architectural judgment when the task leaves structure to the agent |
| `gobstraction-audit` | Whole-change or whole-repo conceptual audit; routes to the relevant lenses |
| `gobstraction-delete` | Abstractions that may be removable indirection |
| `gobstraction-merge` | Two concepts that may actually be one |
| `gobstraction-split` | One concept carrying orthogonal responsibilities |
| `gobstraction-contain` | Compatibility or variant knowledge leaking across callers |
| `gobstraction-zero` | Zero-based test for historical or sunk-cost types |
| `gobstraction-ground` | Formal properties that may not trace to real requirements |
| `gobstraction-compose` | Illegal states from composed state machines; misplaced state or lifecycle ownership |

## Install

This repository follows the layout used by `vercel-labs/skills`: each skill lives at `skills/<skill-name>/SKILL.md` with YAML frontmatter containing `name` and `description`.

From a local checkout:

```bash
npx skills add . --list
npx skills add . --skill '*'
```

From GitHub:

```bash
npx skills add ytfh44/Gobstraction --list
npx skills add ytfh44/Gobstraction --skill '*'
```

## Design

`gobstraction` is intentionally compact and suitable for frequent loading. It contains the architecture decision gate and routes attention to the lens most likely to falsify a proposed design.

The seven lens skills are evidence protocols, not pattern catalogs. A lens may establish a pressure such as “variant knowledge is dispersed”; it does not automatically prescribe Strategy, Adapter, Repository, or any other pattern. The smallest design that removes the demonstrated problem wins.

`gobstraction-audit` selects only the relevant lenses. It should not run all seven by default, and “no architectural change needed” is a valid result.

## Hooks

The draft ships no hooks. The portable skill descriptions are sufficient for harnesses that support semantic skill activation, and a cross-agent hook would add behavior outside the Agent Skills convention. If a specific harness later shows instruction drift or loses rules in subagents, add the smallest harness-specific propagation hook as an adapter rather than making it part of the core method.

## License

MIT.
