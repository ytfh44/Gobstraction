---
name: gobstraction-delete
description: Use when an interface, facade, service, repository, wrapper, factory, adapter, or other abstraction may be unnecessary indirection or speculative flexibility.
---

# Gobstraction: Delete

Ask whether this abstraction represents real variation or policy today.

## Hunt

Look for:

- one runtime implementation
- one or two call sites
- methods that only delegate to another API
- factories with one product
- config with one effective value
- types created for a second use-case that never arrived
- layers whose removal only shortens the call chain

Measure implementation count, call-site count, forwarding/delegation lines, owned state, owned invariants, and polymorphic use.

## Counterfactual

Inline or delete the abstraction mentally. Rewrite each client against the next concrete boundary. Ask exactly what expressive power, invariant, ownership boundary, or substitution capability is lost.

If the answer is “none” and clients become simpler, deletion is supported.

## Do Not False-Positive

One implementation can still justify a boundary when it:

- isolates an external or volatile API
- forms a trust, package, process, or ownership boundary
- owns policy, lifecycle, caching, transactions, or invariants
- is part of a current public compatibility contract
- is required by an active current migration

Test doubles alone are weak evidence for a production abstraction.

## Decision

Return one of:

- **DELETE** — no current semantic capability is lost; state the smallest replacement.
- **KEEP** — name the concrete boundary or invariant it owns.
- **DEFER** — evidence is insufficient; name the missing fact.

Do not replace a deleted abstraction with a differently named equivalent.
