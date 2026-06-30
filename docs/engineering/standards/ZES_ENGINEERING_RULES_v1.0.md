# ZES Engineering Rules v1.0

## Status

Active

---

# Purpose

Define the operational engineering rules that govern how the Ziva Engineering System (ZES) is maintained, extended and audited.

These rules ensure consistency between architecture, documentation and implementation.

---

# Scope

Applies to all engineering activities within ZES:

- ADRs
- Policies
- Standards
- Repository structure
- AI-assisted development
- Documentation updates

---

# Core Engineering Rules

## Rule 1 — Documentation Precedence

Documentation always defines system behavior.

If implementation differs from documentation, documentation prevails.

---

## Rule 2 — No Undocumented Implementation

No code, structure or decision may exist without prior documentation.

---

## Rule 3 — Atomic Change Principle

Each commit must represent a single logical change.

Multiple unrelated changes in one commit are not allowed.

---

## Rule 4 — Traceable Scope

Every change must be traceable to:

- an ADR
- a Policy
- or an explicit Engineering Rule

If not traceable, it is invalid.

---

## Rule 5 — ADR Integrity

ADRs are immutable historical records of decisions.

They can only be:

- extended (new ADR)
- clarified (new ADR)
- corrected via explicit correction ADR

Direct silent modification of meaning is not allowed.

---

## Rule 6 — Structure Consistency

Repository structure must always match declared structure in:

- docs/README.md
- Engineering Charter

Any divergence must be corrected before new features.

---

## Rule 7 — AI Usage Constraint

AI systems used in engineering must:

- follow existing documentation
- not invent architecture
- not bypass ADR logic
- not introduce undocumented assumptions

---

## Rule 8 — Deterministic Design Principle

Systems must behave deterministically at the architectural level:

- same input → same output
- no hidden probabilistic logic in core systems
- no implicit business rules

---

## Rule 9 — Controlled Evolution

System evolution must occur through:

1. Documentation update
2. ADR creation or update
3. Policy adjustment (if required)
4. Implementation

Never skip steps.

---

## Rule 10 — Auditability Requirement

Every part of the system must be:

- explainable
- traceable
- reproducible from documentation alone

If a component cannot be audited from documentation, it is invalid.

---

# Relationship to Other Documents

This document operates under:

- 00_ENGINEERING_CHARTER.md (highest authority)
- Documentation First Policy
- Repository Materialization Policy

And applies to:

- all ADRs
- all engineering policies
- all system implementations

---

# Enforcement

Violations of these rules are treated as:

- architectural inconsistencies
- remediation-required issues
- blockers for implementation phases

---

# Version History

| Version | Date | Description |
|----------|------|-------------|
| 1.0.0 | 2026-06-30 | Initial engineering ruleset |
