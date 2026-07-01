# ARB-0001: FinancialTrustProfile Review

**Status:** closed

**Review Date:** 2026-06-30

**Related ACB:** ACB-0001

---

# Purpose

This Architecture Review Board (ARB) document evaluates the architectural finding recorded as ACB-0001 regarding the exposure of internal identifiers within the FinancialTrustProfile contract.

Its objective is to determine whether the finding represents a genuine architectural inconsistency and to define the official resolution before any modification to the architecture is performed.

---

# Background

Engineering Audit v2 identified that the current FinancialTrustProfile contract contains an internal `userId` field.

The audit concluded that exposing an internal identifier outside the Identity Layer may violate the architectural separation defined by the Identity Model and the Security Model.

The finding was classified as **Critical**.

---

# Documents Reviewed

- ADR-0006 — Identity Layer
- ADR-0011 — Domain Contracts
- ADR-0018 — Security Model

---

# Architectural Question

Should the FinancialTrustProfile expose internal identity references?

---

# Analysis

The review confirms that the concern is valid.

The Identity Layer was intentionally designed to isolate personal identity from financial evidence and trust evaluation.

The Security Model also establishes that internal identifiers must never become externally accessible through business contracts.

Using the same FinancialTrustProfile structure for both internal processing and external consumption creates ambiguity and increases the risk of accidental information disclosure.

Although the current architecture does not explicitly expose the identifier through an API, the contract itself does not distinguish between internal and external usage.

This ambiguity should be removed before implementation begins.

---

# Alternatives Evaluated

## Alternative A — Keep the current contract

Advantages:

- no documentation changes
- no implementation impact

Disadvantages:

- architectural ambiguity remains
- higher privacy risk
- weak separation of concerns

Decision:

Rejected.

---

## Alternative B — Remove `userId` completely

Advantages:

- strongest privacy model
- simplest external contract

Disadvantages:

- internal processing loses stable correlation reference
- additional internal mapping becomes necessary

Decision:

Rejected.

---

## Alternative C — Separate internal and external contracts

Advantages:

- preserves internal processing requirements
- eliminates external exposure
- maintains architectural separation
- aligns with Identity Layer principles
- aligns with Security Model

Disadvantages:

- introduces an additional contract definition
- requires documentation updates

Decision:

Approved.

---

# Architecture Board Decision

The Architecture Review Board approves **Alternative C**.

The system shall distinguish between:

- Internal Financial Trust Profile
- External Financial Trust Profile

Internal contracts may contain internal correlation identifiers.

External contracts must never expose internal identifiers.

This distinction shall become part of the official architecture before implementation begins.

---

# Required Documentation Updates

The following documents require controlled updates:

- ADR-0011
- ADR-0006 (clarification if required)
- ADR-0018 (cross-reference if required)

No implementation work may begin until these updates are completed.

---

# Impact Assessment

Implementation Impact:

Low.

Architecture Impact:

Low.

Security Impact:

High positive impact.

Privacy Impact:

High positive impact.

Maintainability Impact:

Positive.

---


# Resolution

Architecture finding accepted.

Controlled documentation update required.

ACB-0001 remains **In Review** until all documentation updates are completed.

---

# Guiding Principle

> Internal identifiers exist to support system operation, not external visibility.

---

---

## Closure Summary

ARB-0001 is closed following successful resolution of all dependent architectural requirements.

### Resolved Dependencies

- ACB-0001 completed (Financial Trust Profile split enforcement)
- ADR-0011 updated to enforce internal/external FTP separation
- Identity isolation rules fully implemented
- External exposure of internal identifiers eliminated

---

## Final Outcome

- Financial Trust Profile architecture is compliant
- Internal and external contract boundaries are formally enforced
- No remaining dependency blockers on this ARB

---

## Certification Impact

ARB-0001 no longer blocks Foundation Certification.

> Status: Closed and resolved

# Version

1.0.0
