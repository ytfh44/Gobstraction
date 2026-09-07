---
name: gobstraction-merge
description: Use when two types, enums, models, DTOs, hierarchies, or state concepts look structurally duplicated or require trivial bidirectional mapping to stay synchronized.
---

# Gobstraction: Merge

Ask whether two names encode one invariant or merely share a shape.

## Hunt

Look for:

- mostly identical fields and behavior
- parallel hierarchies
- trivial `a.x = b.x` mapping in both directions
- mirrored enums or synchronized switch statements
- duplicated validation and transition rules
- renames that preserve every invariant

Build a structural comparison: fields, types, defaults, validation, lifecycle, authority, transitions, and consumers. Inspect mapper code and count synchronized cases.

## Counterfactual

Rename both concepts to one neutral name and delete the mappers. Could every caller still state its meaning without casts, hidden validation, or boundary-specific rules? Could one type be an alias of the other without changing who owns or trusts the data?

## Do Not False-Positive

Do not merge merely because shapes match when the concepts differ in:

- trust or validation boundary
- authority or source of truth
- lifecycle or mutability
- units or semantic interpretation
- privacy or serialization contract
- domain invariant

An external request type and an internal domain type may be intentionally isomorphic.

## Decision

Return:

- **MERGE** — same invariant and ownership; delete trivial mapping.
- **KEEP DISTINCT** — name the semantic boundary that differs.
- **DEFER** — identify the missing invariant or ownership evidence.

Prefer one concept over two synchronized synonyms, but never erase a real boundary to remove boilerplate.
