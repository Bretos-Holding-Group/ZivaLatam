# Governance Authority Rules — ZES

## Version
1.0.0

## Status
Active

## Purpose

This document defines the authoritative hierarchy and consistency rules for governance state management across the ZES system.

It establishes the single source of truth model for system state resolution, conflict handling, and certification eligibility.

---

# 1. Governance Hierarchy

The system defines a strict hierarchical model:

## 1.1 ARB — Architectural Review Board (TRUTH LAYER)

ARB is the **only authoritative source of system state**.

ARB defines:

- FINAL status of architectural decisions
- Closure of ACB items
- System-level resolution states

### Valid ARB States:
- CLOSED
- OPEN
- REJECTED
- PARTIAL
- DEFERRED

### Authority Rule:
> ARB overrides all other governance layers regarding state.

---

## 1.2 ACB — Architectural Control Block (TRACKING LAYER)

ACB is a **tracking and execution observation layer**.

ACB defines:

- Work items derived from architectural decisions
- Implementation tracking of ADR-driven changes
- Operational progress visibility

### ACB States:
- In Review
- In Progress
- Resolved
- Stale (derived state, not manually assigned)

### Authority Rule:
> ACB does NOT define system truth. It only reflects implementation status.

---

## 1.3 ADR — Architecture Decision Record (DESIGN LAYER)

ADR defines **intent and design only**.

ADR defines:

- Architectural decisions
- System design constraints
- Contract definitions

### Authority Rule:
> ADR does NOT define state or closure conditions.

---

# 2. Source of Truth Rule

## 2.1 Single Truth Principle

> ARB is the only source of truth for system state.

If ARB state conflicts with any ACB state:

- ARB ALWAYS takes precedence
- ACB is marked as STALE
- No certification failure is triggered solely by ACB mismatch

---

## 2.2 State Resolution Priority

| Priority | Layer | Authority |
|----------|------|----------|
| 1 | ARB | Absolute truth |
| 2 | ACB | Operational tracking |
| 3 | ADR | Design specification |

---

# 3. Consistency Rules

## 3.1 ACB → ARB Binding Requirement

Every ACB MUST reference a corresponding ARB entry.

If no ARB exists:

- ACB is INVALID for certification purposes
- Certification gate fails

---

## 3.2 ARB Overrides Rule

If:

- ARB = CLOSED
- ACB = In Review

Then:

- ACB is considered STALE (not blocking)
- System state remains VALID if ARB closure is consistent

---

## 3.3 Invalid State Condition

A system is INVALID if:

- ARB and ACB explicitly contradict FINAL state semantics
  (example: ARB CLOSED vs ACB REJECTED with no reconciliation note)

---

# 4. Certification Eligibility Rules

ZES Foundation Certification is eligible ONLY if:

- All critical ACBs have corresponding ARBs
- No unresolved ARB contradictions exist
- No missing ARB references for critical ACBs
- RSBL references are consistent in core ADRs (where required)

---

# 5. Governance Integrity Rules

## 5.1 No Silent State Drift

State changes MUST be reflected in ARB explicitly.

No implicit state updates via:

- ADR text changes
- ACB comments
- documentation prose

---

## 5.2 No Dual Truth Sources

The system MUST NOT interpret:

- ACB as truth
- ARB as truth

simultaneously.

ARB is the only truth layer.

---

## 5.3 Determinism Requirement

All governance state resolution MUST be:

- deterministic
- reproducible
- traceable to ARB entries

---

# 6. Staleness Definition

An ACB is considered **STALE** when:

- ARB state differs from ACB state
- ARB defines closure but ACB remains open
- ACB has no updated synchronization after ARB resolution

Stale ACBs do NOT block certification unless ARB is missing or inconsistent.

---

# 7. Security and Auditability Rule

Governance state MUST:

- be traceable from ARB
- not rely on descriptive text
- avoid ambiguity between status fields and narrative descriptions

Only structured ARB fields are valid for audit decisions.

---

# 8. Migration Rule (Applies Immediately)

Upon adoption of this document:

- ARB becomes authoritative for all historical ACB state interpretation
- ACB fields are downgraded to observational metadata
- ADRs remain unaffected in semantic role

---

# 9. Final Principle

> Governance truth is not distributed. It is anchored.

ARB is that anchor.
