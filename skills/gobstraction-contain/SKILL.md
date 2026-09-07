---
name: gobstraction-contain
description: Use when callers repeatedly branch on legacy/version/type/feature variants, compatibility knowledge is dispersed, or an abstraction appears to leak its internal variants into clients.
---

# Gobstraction: Contain

Variant knowledge should live at the narrowest boundary that genuinely needs it.

## Hunt

Search for repeated:

- `legacy`, `compat`, `v1`, `v2`, migration flags
- `instanceof`, type/tag checks, subtype switches
- feature-flag branches for implementation variants
- TODO branches intended to disappear after migration

Record branch-site count, distinct files/callers, variant names, and how far the knowledge is dispersed from the boundary that introduces the variant.

## Diagnosis

If unrelated callers must know which internal variant they received, the abstraction is not containing variation.

Centralize the decision at the narrowest stable boundary. The result may be one function, one adapter, one decoder, or polymorphism; choose the smallest representation justified by actual variation.

## Counterfactual

Remove variant knowledge from every caller except one boundary. Can callers operate on a stable semantic operation instead? If yes, centralization is supported.

## Do Not False-Positive

Keep an explicit branch when it is already:

- the single protocol decoding boundary
- one exhaustive domain match that makes semantics clearer
- required at a UI or policy boundary where the variants genuinely mean different things

Do not replace one clear `if version` with a hierarchy that has no independent behavior.

## Decision

Return:

- **CENTRALIZE** — identify the boundary and repeated knowledge to remove.
- **KEEP LOCAL** — explain why the caller legitimately owns the distinction.
- **DEFER** — state what variation/ownership evidence is missing.
