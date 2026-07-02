# ACB-0003 — Credit Domain Formalization

## Status
In Review

## Context
Credit Domain is defined in ADR-0023 but lacks consistent enforcement of identity isolation rules across internal and external contracts.

## Issue
- CreditSignal includes userId without explicit internal/external separation
- Risk of identity leakage through downstream consumers
- Missing structural parity with FTP split (ADR-0011)

## Required Actions
- Introduce CreditSignalInternal / CreditSignalExternal model
- Enforce identity isolation rules from ADR-0011
- Validate output contract separation for external systems

## Dependency
ADR-0023 Credit Domain Architecture

## Outcome
Credit Domain becomes fully privacy-safe and structurally consistent with system-wide contract rules
