# Source-to-ADR Mapping

## Status

Active

---

## Purpose

This document establishes the authoritative mapping between the implementation structure (`src/`) and the Architecture Decision Records (ADRs) that govern each architectural component.

Its purpose is to guarantee complete traceability between architecture and implementation.

No implementation directory SHALL exist without architectural governance.

---

# Governing Principle

> Every implementation component MUST be traceable to at least one approved Architecture Decision Record before implementation begins.

---

# Mapping

| Implementation Path | Governing ADR(s) | Status |
|---------------------|------------------|--------|
| `src/kernel/` | ADR-0022 | Governed |
| `src/contracts/` | ADR-0011 | Governed |
| `src/domains/evidence/` | ADR-0004, ADR-0011 | Governed |
| `src/domains/trust/` | ADR-0005, ADR-0011, ADR-0016 | Governed |
| `src/domains/credit/` | ADR-0023 | Governed |
| `src/domains/intelligence/` | ADR-0024 | Governed |

---

# Coverage Rule

Every implementation directory SHALL satisfy all of the following conditions:

- be formally documented;
- be governed by one or more approved ADRs;
- have clearly defined responsibilities;
- have clearly defined architectural boundaries;
- comply with Domain Contracts where applicable;
- satisfy Foundation Certification requirements.

Directories failing any of these conditions SHALL be considered non-compliant.

---

# Traceability Rule

Architecture governs implementation.

Implementation SHALL NEVER become the source of architectural authority.

Whenever a new implementation directory is introduced:

1. The architectural decision SHALL be documented first.
2. The corresponding ADR SHALL be approved.
3. This mapping SHALL be updated.
4. Only then MAY implementation begin.

---

# Relationship with Foundation Certification

This document supports Foundation Certification by providing explicit traceability between:

- architectural governance;
- implementation structure;
- certification scope.

It eliminates undocumented implementation areas and reduces architectural drift.

---

# Relationship with Architecture Governance

This document complements:

- Architecture Decision Records (ADR)
- Architecture Review Board (ARB)
- Architecture Consolidation Backlog (ACB)

It does not replace any governance artifact.

---

# Maintenance

This document SHALL be updated whenever:

- a new implementation directory is created;
- an existing implementation directory changes architectural ownership;
- an ADR supersedes another ADR;
- implementation scope changes.

---

# Success Criteria

The mapping is considered complete when:

- every directory under `src/` is governed;
- no undocumented implementation exists;
- every implementation component is traceable;
- Foundation Certification can verify implementation coverage without ambiguity.

---

# Core Principle

> Architecture defines the system. Implementation realizes it. Traceability connects both.
