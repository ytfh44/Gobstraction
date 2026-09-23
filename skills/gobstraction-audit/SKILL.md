---
name: gobstraction-audit
description: Use when reviewing a repository, subsystem, refactor, or architectural change for conceptual integrity, unnecessary abstractions, misplaced boundaries, or composition risks.
---

# Gobstraction Audit

Audit concepts, not style. Do not assume every lens must produce a finding.

## 1. Scope the Architectural Delta

Classify the change or area:

- local implementation only
- API or data-model boundary
- abstraction introduction or deletion
- compatibility or migration
- formal model or invariant
- state or lifecycle ownership
- multiple stateful subsystems
- broad structural refactor

If it is purely local implementation with no architectural discretion, stop unless the user explicitly requested an audit.

## 2. Select Lenses

Use only the smallest relevant set, normally 1-3:

| Signal | Lens |
| --- | --- |
| one implementation, wrapper, forwarding layer | `gobstraction-delete` |
| duplicate types, mappers, synchronized enums | `gobstraction-merge` |
| disjoint method/dependency clusters | `gobstraction-split` |
| repeated legacy/version/tag branches | `gobstraction-contain` |
| historical/framework residue | `gobstraction-zero` |
| theorem/spec with unclear requirement trace | `gobstraction-ground` |
| interacting state machines/protocols | `gobstraction-compose` |
| state or lifecycle owned by the wrong component; local failure forcing remote recovery | `gobstraction-compose` |

When two lenses pull in opposite directions, treat that as useful evidence. Example: `split` may discover two real responsibilities while `delete` shows that two new interfaces would still be unjustified.

## 3. Report Findings

For each finding provide:

- **Claim** — one falsifiable architectural statement.
- **Evidence** — counts, call sites, mappings, branches, dependencies, history, reachable states, or transition and failure-propagation paths.
- **Counterfactual** — mentally delete/merge/split/centralize/rebuild, or relocate ownership, and state what semantic capability changes.
- **Risk** — what boundary or invariant could make the proposed simplification wrong.
- **Decision** — keep, change, or defer for insufficient evidence.

Rank by semantic impact and blast radius, not by lines changed.

## Rules

No finding is better than an invented finding. Future flexibility without a current requirement is not evidence. A discovered problem does not imply a named design pattern; choose the smallest representation that removes the demonstrated problem.
