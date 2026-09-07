---
name: gobstraction-split
description: Use when one class, module, service, manager, aggregate, or stateful component appears to change for independent reasons or mixes orthogonal policy, lifecycle, persistence, parsing, validation, coordination, or state concerns.
---

# Gobstraction: Split

Find concept-level responsibility collisions, not merely large files.

## Hunt

List independent reasons the concept changes. Look for:

- method clusters with disjoint dependencies
- business policy mixed with persistence mechanics
- parsing mixed with semantic validation
- lifecycle mixed with policy
- coordination mixed with durable state
- two independent extension axes modifying the same type
- unrelated commits repeatedly touching the same file

A useful split separates change axes that can vary independently.

## Counterfactual

Imagine changing axis A while freezing axis B, then changing B while freezing A. If each change forces edits through the same concept for no semantic reason, a split is supported.

Propose the narrowest ownership boundary that would let those changes vary independently.

## Do Not False-Positive

Do not split because:

- a file is long
- a class has many methods that share one invariant
- two implementation details happen to use different libraries
- “SRP” would look cleaner on a diagram

A small cohesive component may legitimately perform several steps of one responsibility. A split that adds indirection without reducing coupling fails the test.

## Decision

Return:

- **SPLIT** — name the two independent change axes and their smallest useful boundary.
- **KEEP TOGETHER** — show the shared invariant or lifecycle that makes them one concept.
- **DEFER** — name the history, dependency, or ownership evidence still needed.

After proposing a split, apply the deletion test mentally: do not create interfaces or layers that have no current variation.
