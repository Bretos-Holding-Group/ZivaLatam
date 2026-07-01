# ADR-0021 — Architecture Backlog and Certification Scope Alignment

**Status:** Accepted  
**Type:** Architecture Decision Record  
**Domain:** Governance / Architecture Integrity  
**Supersedes:** N/A  
**Related:** ADR-0014, ADR-0019, ARB-0001

---

# 1. Context

The ZES system has evolved into a multi-domain architecture including:

- Kernel Layer (`src/kernel`)
- Contracts Layer (`src/contracts`)
- Evidence Domain
- Trust Domain
- Credit Domain (declared but not formally governed)
- Intelligence Domain (declared but not formally governed)

During recent audits, multiple inconsistencies were identified between:

- implementation structure (`src/`)
- ADR governance layer
- architectural backlog references (ACB)
- certification requirements (Foundation Certification)

A formal consolidation layer is required to reconcile implementation reality with governance documentation.

---

# 2. Problem

The system currently exhibits:

- implementation structures without corresponding ADR definitions
- ADRs referencing outdated system scope ranges (0001–0019 vs 0001–0021)
- missing Architecture Consolidation Backlog (ACB-0001)
- certification dependency on incomplete governance alignment
- undefined boundaries for Kernel, Credit, and Intelligence domains

This results in:

> broken traceability between system implementation and governance authority

---

# 3. Decision

A formal Architecture Consolidation Backlog (ACB) scope is introduced.

This ADR defines the scope required to complete system alignment prior to Foundation Certification execution.

---

# 4. ACB Scope Definition

The Architecture Consolidation Backlog includes:

## ACB Items:

- ACB-0001 → FTP contract structural correction (userId separation)
- ACB-0002 → Kernel architectural formalization (ADR-0022)
- ACB-0003 → Credit Domain formalization (ADR-0023)
- ACB-0004 → Intelligence Domain formalization (ADR-0024)
- ACB-0005 → ADR range synchronization (0001 → 0021 consistency)
- ACB-0006 → Contract versioning enforcement (ADR-0011 compliance)
- ACB-0007 → Environmental Efficiency principle formalization or removal
- ACB-0008 → RSBL cross-reference integration across governance layers

---

# 5. Certification Dependency Rule

The Foundation Certification process MUST NOT execute unless:

- ACB-0001 to ACB-0008 are either:
  - Resolved OR
  - Explicitly deferred via ADR update

---

# 6. System Impact

This ADR establishes:

- a formal pre-certification alignment layer
- a dependency gate before Foundation Certification
- a traceability bridge between implementation and governance

---

# 7. Relationship to Existing System

This ADR does NOT introduce new architecture.

It formalizes:

- previously identified audit findings
- ARB-0001 decision scope
- Foundation Certification prerequisites

---

# 8. Governance Effect

After this ADR:

- ACB becomes a first-class governance construct
- certification is blocked until backlog closure
- implementation must map to ADR coverage

---

# 9. Outcome

- System scope is now formally bounded to ADR-0001 → ADR-0021
- Certification process gains explicit dependency gate
- Architectural drift between src/ and ADR layer is controlled

---

# 10. Notes

This ADR is a stabilization mechanism.

It does not change architecture — it enforces alignment between design and implementation.
