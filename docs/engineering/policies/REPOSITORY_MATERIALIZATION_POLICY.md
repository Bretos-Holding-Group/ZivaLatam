# Repository Materialization Policy

## Status

Active

---

## Purpose

Ensure that every permanent engineering decision, architectural definition, policy, standard, workflow and product specification becomes part of the repository.

The repository is the institutional memory of Ziva Latam.

Knowledge must never depend exclusively on conversations or individual contributors.

---

## Scope

This policy applies to:

- Human contributors
- AI assistants
- External collaborators
- Engineering documentation
- Architecture documentation
- Product documentation
- Governance documentation

---

## Policy Statement

> No engineering knowledge is considered official until it has been materialized in the repository.

---

## Rules

### Rule 1 — Repository as Source of Truth

The Git repository is the only official source of engineering knowledge.

Chat conversations are temporary working spaces.

Only repository content is considered official.

---

### Rule 2 — Materialization Required

Any approved decision must be transformed into one or more repository artifacts.

Examples:

- ADR
- Policy
- Standard
- Product document
- Workflow
- Technical specification

---

### Rule 3 — No Orphan Knowledge

Important decisions must never remain only in:

- chat history;
- personal notes;
- AI conversations;
- verbal agreements.

---

### Rule 4 — Purpose Before Existence

Every new file or directory must have a clearly documented purpose.

Directories must never exist without at least one meaningful artifact explaining their function.

---

### Rule 5 — Traceability

Every engineering artifact must be traceable to its origin.

Possible origins include:

- Engineering Charter
- Approved ADR
- Engineering Policy
- Product Vision
- Approved engineering decision

---

### Rule 6 — Institutional Memory

The repository represents the institutional memory of Ziva Latam.

Future contributors must be able to understand the project without depending on its original creators.

---

## Exceptions

Temporary working notes are allowed during active discussions.

Once approved, relevant knowledge must be materialized in the repository before implementation continues.

---

## Compliance

Compliance is verified during:

- Documentation Review
- Architecture Review
- Engineering Audit

Artifacts that exist only outside the repository are considered unofficial.

---

## Related Documents

- 00_ENGINEERING_CHARTER.md
- POLICY_TEMPLATE.md
- DOCUMENTATION_FIRST_POLICY.md
- All ADRs

---

## Change History

| Version | Date | Description |
|---------|------|-------------|
| 1.0.0 | 2026-06-30 | Initial version |
