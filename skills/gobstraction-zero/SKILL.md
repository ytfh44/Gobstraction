---
name: gobstraction-zero
description: Use when an existing type, base class, layer, framework pattern, compatibility object, or architectural concept may survive only because of historical constraints or sunk cost.
---

# Gobstraction: Zero

Ask what would exist if today's requirements were the starting point.

## Zero-Based Model

Without copying the current class/module diagram, describe the current system in 3-5 core concepts. Base them on user-visible requirements, external contracts, invariants, and real variation.

Then compare suspect existing concepts against that model.

## Evidence

Collect:

- original historical rationale if available
- whether that constraint still exists
- current callers and responsibilities
- migration or compatibility obligations
- learning/indirection cost of keeping it
- concrete benefit it still provides

A large caller count is not proof of conceptual necessity; callers may simply have grown around an obsolete boundary.

## Counterfactual

Design the relevant slice from zero for current requirements. Would this concept reappear naturally? If not, what direct structure replaces it, and what compatibility work is required to retire it safely?

## Do Not False-Positive

Historical origin does not make a concept obsolete. Keep it while it still represents:

- an external/public contract
- persisted data compatibility
- an active migration
- regulatory or operational constraints
- a real current ownership boundary

## Decision

Return:

- **RETIRE** — current requirements no longer justify the concept; give the smallest migration path.
- **KEEP** — identify the current constraint that still recreates it from zero.
- **DEFER** — identify the historical or compatibility fact that must be checked.

Do not rewrite a working architecture merely because a prettier clean-sheet diagram exists.
