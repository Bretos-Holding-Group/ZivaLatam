# AI Collaboration Policy

## Status

Active

---

## Purpose

Define the operational rules governing the collaboration between human contributors and Artificial Intelligence (AI) systems within the Ziva Engineering System (ZES).

The objective is to ensure that AI accelerates engineering activities while preserving architectural consistency, security, documentation quality and human accountability.

---

## Scope

This policy applies to:

- AI assistants
- Human contributors
- External collaborators
- Engineering activities
- Product documentation
- Architecture
- Software implementation
- Code review

---

## Policy Statement

> AI is an engineering collaborator, never the final decision-maker.

Final responsibility always belongs to the authorized human decision-makers.

---

## Principles

### Human Accountability

Humans remain responsible for every approved decision.

AI may recommend.

Humans approve.

---

### Documentation Before Generation

AI must never generate implementation before the required documentation exists.

---

### Architectural Consistency

AI must preserve the approved architecture.

AI shall not introduce patterns, frameworks or technologies that contradict accepted ADRs or Engineering Policies.

---

### Explain Before Implement

Whenever possible, AI should explain the reasoning behind its recommendations before proposing implementation.

The objective is to educate contributors, not simply generate artifacts.

---

### Simplicity First

AI should recommend the simplest solution capable of satisfying the approved requirements.

Complexity must always be justified.

---

## Rules

### Rule 1 — AI Cannot Expand Scope

AI must never introduce features outside the approved roadmap.

Any new idea must be registered for future evaluation.

---

### Rule 2 — AI Must Respect Approved Documentation

Engineering documentation has priority over AI assumptions.

When documentation and AI reasoning conflict, documentation prevails.

---

### Rule 3 — AI Must Declare Uncertainty

If information is incomplete, AI must explicitly identify assumptions instead of inventing missing details.

---

### Rule 4 — No Hidden Decisions

AI must never make silent architectural decisions.

Significant decisions require documentation and approval.

---

### Rule 5 — Knowledge Transfer

AI should strengthen the engineering capabilities of contributors by explaining concepts, trade-offs and consequences whenever appropriate.

---

### Rule 6 — Repository First

Approved knowledge must be materialized in the repository.

Conversations are temporary.

The repository is permanent.

---

## Exceptions

No exceptions are defined.

Any exception requires explicit approval and documentation.

---

## Compliance

Compliance is verified through:

- Architecture Reviews
- Documentation Reviews
- Engineering Audits
- Pull Request Reviews

---

## Related Documents

- 00_ENGINEERING_CHARTER.md
- DOCUMENTATION_FIRST_POLICY.md
- REPOSITORY_MATERIALIZATION_POLICY.md
- MVP_FREEZE_POLICY.md
- All accepted ADRs

---

## Change History

| Version | Date | Description |
|---------|------|-------------|
| 1.0.0 | 2026-06-30 | Initial version |
