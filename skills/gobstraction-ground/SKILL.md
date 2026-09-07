---
name: gobstraction-ground
description: Use when reviewing formal specifications, invariants, proofs, model checking, property tests, or verification claims whose connection to external requirements or real failure modes is unclear.
---

# Gobstraction: Ground

A proof is useful when it constrains a real failure mode, not merely when it follows from definitions.

## Trace Properties Outward

For every proved property or invariant, record:

- the theorem/property statement
- definitions or assumptions it depends on
- the original requirement, user-visible guarantee, or operational risk it claims to cover
- a concrete bug or bad behavior it rules out

Build a requirement-to-property trace. Gaps deserve attention even when every proof passes.

## Vacuity Tests

Ask:

- Is the theorem a restatement of a definition?
- Did assumptions exclude the failure mode being claimed away?
- Could a clearly unacceptable implementation still satisfy the model?
- Does the property mention the resource, actor, timing, authority, or environment constraint present in the real requirement?

Demand a counterexample: describe one real bug the current model would still allow.

## Do Not False-Positive

In a mathematical library, a theorem may itself be the external product requirement. Do not require a business story where the theorem is the intended artifact.

A simple property is not vacuous merely because its proof is easy.

## Decision

Return:

- **GROUNDED** — trace to a real requirement and named failure mode is clear.
- **VACUOUS** — proof follows without constraining the claimed real behavior.
- **UNDER-SPECIFIED** — relevant failure modes remain permitted; name the missing property.
- **DEFER** — requirement provenance is unavailable.

Strengthen the specification before adding more proof machinery.
