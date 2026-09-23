---
name: gobstraction-compose
description: Use when two or more state machines, workflows, protocols, lifecycles, or independently valid stateful components interact; when a state, fact, or lifecycle may be owned by the wrong component; or when a design has no illegal reachable state yet pays for cross-machine recovery.
---

# Gobstraction: Compose

Local validity does not imply global validity.
Correct composition does not imply correct ownership.

## Ownership and Lifetime Check

Run before the product-state check whenever more than one component holds state, or a lifecycle is being assigned.

1. For each semantic fact and lifecycle, name its authoritative owner. Classify every other copy as derived observation, cache, replica, lease, proposal, checkpoint, log, or resource residency; divergence of a non-authoritative copy from its owner is not a defect.
2. Name who may create, pause, resume, destroy, and recover it, and in which phase that authority holds. Authority belongs to (fact, phase), not permanently to a component.
3. Separate lifetimes that are easy to conflate: identity, semantic/execution, resource residency, durable storage. `alive` does not imply `resident`; membership in an owner's table or in an address space does not imply physical presence.
4. For each lifecycle transition (create, pause, resume, destroy, fail, restart, evict, retry), list which other machines must also transition, reconcile, replay, or roll back, and whether that dependency follows from domain semantics or only from the current ownership boundary.
5. If a state's semantic lifetime outlives its owner, or a local failure forces unrelated remote recovery, test moving ownership or splitting the lifetime before adding coordination.
6. Name the dominant constraint under which the current ownership is correct — the process or state that is currently most expensive or hardest to reconstruct. If that constraint has moved, the ownership is stale, not merely imperfect.

## Product-State Check

For interacting machines A and B:

1. List their states and transition guards.
2. Consider reachable pairs in `StateA x StateB`; avoid enumerating impossible pairs blindly when reachability can prune them.
3. Mark combinations that are locally valid but violate a cross-system business, safety, authority, or lifecycle invariant.
4. Trace whether each illegal combination is actually reachable under current transitions, concurrency, retries, and failure paths, and whether it is amplified by a barrier, batch, or repeated step.

For large systems, analyze only the coupled state dimensions and the transitions that cross their boundary.

## Evidence

Produce a small table with:

- composite state
- reachable?
- globally legal?
- transition/path that reaches it
- missing guard or invariant

When ownership is in question, add a second small table:

- transition
- machines forced to transition, reconcile, replay, or roll back
- domain-required or ownership-induced?
- amplified by a barrier, batch, or iteration?

Examples include paid+cancelled without refund, connected+logged-out when authorization is required, or committed+unreplicated when durability promises forbid it.

## Counterfactual

For an illegal state: add the smallest cross-machine invariant or guard that forbids the demonstrated path, and recompute reachability around that path.

For a wrong owner: move ownership, split the lifetime, make one copy derived, or remove duplicated authority — in that order — before adding a guard, protocol, or coordinator. Adding synchronization to preserve a wrong boundary is not a fix.

## Do Not False-Positive

A Cartesian-product combination is not a bug if it is unreachable by construction. Show the path before proposing coordination.

Do not create a god coordinator merely because two machines interact. Prefer a local joint guard, explicit transition, hierarchical state, or boundary protocol when sufficient.

A stale observation, cache, replica, lease, or speculative placement is not divergence to synchronize. Only authoritative states must agree.

Ownership that was correct under a past dominant constraint is not wrong today unless that constraint has moved; name the constraint before proposing a move.

Untrusted is not malicious. A trust assumption is a design parameter with an economic optimum: raise isolation only when `probability(misbehavior) x damage` exceeds its cost, and only as far as the blast radius justifies.

Before returning SAFE BY CONSTRUCTION, describe one bad architecture this check would still pass. If that is the design under review, the verdict is not SAFE.

## Decision

Return:

- **ADD INVARIANT/GUARD** — illegal state is reachable; name the smallest constraint.
- **RESTRICT ADMISSION** — the illegal combination can be made unconstructible at creation (eligibility or closure test) instead of guarded later.
- **RELOCATE OWNERSHIP / SPLIT LIFETIME** — no illegal state is reachable, but a local transition forces unrelated remote recovery; name the boundary that should move and the dominant constraint that justifies it.
- **COORDINATE** — correctness truly requires a shared transition owner.
- **SAFE BY CONSTRUCTION** — prove why suspect combinations are unreachable.
- **DEFER** — transition or concurrency semantics are missing.
