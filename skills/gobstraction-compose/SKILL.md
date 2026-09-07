---
name: gobstraction-compose
description: Use when two or more state machines, workflows, protocols, lifecycles, or independently valid stateful components interact and may admit globally illegal combinations or transitions.
---

# Gobstraction: Compose

Local validity does not imply global validity.

## Product-State Check

For interacting machines A and B:

1. List their states and transition guards.
2. Consider reachable pairs in `StateA x StateB`; avoid enumerating impossible pairs blindly when reachability can prune them.
3. Mark combinations that are locally valid but violate a cross-system business, safety, authority, or lifecycle invariant.
4. Trace whether each illegal combination is actually reachable under current transitions, concurrency, retries, and failure paths.

For large systems, analyze only the coupled state dimensions and the transitions that cross their boundary.

## Evidence

Produce a small table with:

- composite state
- reachable?
- globally legal?
- transition/path that reaches it
- missing guard or invariant

Examples include paid+cancelled without refund, connected+logged-out when authorization is required, or committed+unreplicated when durability promises forbid it.

## Counterfactual

Add the smallest cross-machine invariant or guard that forbids the demonstrated path. Recompute reachability around that path.

## Do Not False-Positive

A Cartesian-product combination is not a bug if it is unreachable by construction. Show the path before proposing coordination.

Do not create a god coordinator merely because two machines interact. Prefer a local joint guard, explicit transition, hierarchical state, or boundary protocol when sufficient.

## Decision

Return:

- **ADD INVARIANT/GUARD** — illegal state is reachable; name the smallest constraint.
- **COORDINATE** — correctness truly requires a shared transition owner.
- **SAFE BY CONSTRUCTION** — prove why suspect combinations are unreachable.
- **DEFER** — transition or concurrency semantics are missing.
