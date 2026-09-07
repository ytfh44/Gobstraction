---
name: gobstraction
description: Use when a coding task leaves architecture, boundaries, abstractions, data models, compatibility strategy, or state ownership to the agent's discretion.
---

# Gobstraction

Existing code boundaries are evidence, not authority. Infer concepts from current requirements, invariants, actual variation, and composition constraints.

## Architectural Delta Gate

Before introducing, preserving, deleting, merging, or splitting a concept:

1. Name the current requirement or invariant that requires it.
2. Name the simpler representation rejected and what meaning or correctness it loses.
3. Pick the lens most likely to falsify the preferred design.
4. Gather evidence proportional to blast radius; imagined future use-cases are not evidence.
5. Make the smallest change that preserves demonstrated semantics.

## Route

- removable indirection -> `gobstraction-delete`
- duplicate concepts/mappers -> `gobstraction-merge`
- orthogonal responsibilities -> `gobstraction-split`
- scattered legacy/version/type branches -> `gobstraction-contain`
- historical/framework residue -> `gobstraction-zero`
- weakly grounded proof/spec -> `gobstraction-ground`
- interacting state machines -> `gobstraction-compose`
- broad review -> `gobstraction-audit`

## Guardrails

A lens identifies pressure, not a design pattern. Do not materialize every concept you can name. Preserve real trust, authority, lifecycle, compatibility, and domain boundaries. If the current design already represents the real constraints adequately, leave it alone.
