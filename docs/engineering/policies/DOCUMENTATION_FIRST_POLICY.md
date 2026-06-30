# Documentation First Policy

## Status

Active

---

## Purpose

Establish Documentation First as the mandatory engineering practice throughout the Ziva Engineering System (ZES).

The objective is to ensure that every engineering artifact is designed, reviewed and documented before implementation begins.

---

## Scope

This policy applies to:

- Engineering
- Architecture
- Product Design
- Documentation
- Artificial Intelligence
- Security
- Governance

---

## Policy Statement

> No implementation shall begin until the corresponding documentation has been created, reviewed and approved.

Documentation is considered an engineering artifact, not an optional activity.

---

## Rules

### Rule 1 — Documentation Before Code

No production code may be written before the required documentation exists.

---

### Rule 2 — Documentation Defines Implementation

Implementation follows documentation.

Documentation never follows implementation.

---

### Rule 3 — Every Artifact Has Documentation

Every significant engineering artifact must have corresponding documentation.

Examples include:

- Architecture
- APIs
- Domain Contracts
- Security Rules
- Trust Models
- Data Models
- Engineering Standards

---

### Rule 4 — Documentation Is Versioned

Engineering documentation must be maintained under version control within the official repository.

---

### Rule 5 — Documentation Must Be Reviewed

Documentation shall be reviewed before implementation begins.

Approval follows the governance model defined by the Engineering Charter and Decision Escalation Policy.

---

### Rule 6 — AI Must Respect Documentation

Artificial Intelligence assistants must always prioritize approved documentation over assumptions or generated solutions.

When documentation and generated output conflict, documentation prevails.

---

### Rule 7 — Living Documentation

Documentation evolves together with the system.

Every significant engineering change must include corresponding documentation updates.

---

## Exceptions

Exceptions are permitted only for:

- Critical security incidents
- Critical production outages

All exceptions must:

- be documented;
- include justification;
- identify the approving authority;
- be reviewed after resolution.

---

## Compliance

Compliance is verified during:

- Architecture Reviews
- Documentation Reviews
- Engineering Audits
- Pull Request Reviews

Failure to comply with this policy is considered a governance violation.

---

## Related Documents

- 00_ENGINEERING_CHARTER.md
- REPOSITORY_MATERIALIZATION_POLICY.md
- MVP_FREEZE_POLICY.md
- AI_COLLABORATION_POLICY.md
- DECISION_ESCALATION_POLICY.md

---

## Change History

| Version | Date | Description |
|---------|------|-------------|
| 1.0.0 | 2026-06-30 | Initial version |
