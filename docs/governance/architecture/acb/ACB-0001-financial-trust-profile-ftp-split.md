# ACB-0001 — Financial Trust Profile (FTP) Split

## Status
Resolved

## Context
The FinancialTrustProfile currently exposes `userId` in external-facing structures.

This violates system principles of least knowledge and identity isolation.

## Required Fix
Split FTP into two contracts:

### Internal
- FinancialTrustProfileInternal
- Contains userId
- Used only inside Trust system

### External
- FinancialTrustProfileExternal
- MUST NOT contain userId
- Used for APIs and external systems

## Constraint
No external system may access internal identifiers.

## Dependency
This change must be reflected in ADR-0011 before certification.

## Outcome
Enables privacy-safe financial data exposure model.

---

## Closure Note

This ACB is officially closed after:

- ADR-0011 was updated to enforce FTP internal/external split
- FinancialTrustProfileInternal and FinancialTrustProfileExternal were implemented at contract level
- Identity isolation rules were enforced across system boundaries

No further action required.

> ACB-0001 is resolved and closed.
