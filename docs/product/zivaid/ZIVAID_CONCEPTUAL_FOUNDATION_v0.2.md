# ZivaID — Conceptual Foundation v0.2

**Status:** Independently verified and merged baseline
**Version:** 0.2
**Product:** ZivaID
**Brand / ecosystem:** Ziva / ZivaLatam
**Legal-entity naming convention:** ZivaLatam [jurisdiction] SpA, when a jurisdiction-specific legal entity must be distinguished
**Holding:** Breto's Holding Group (BHG)
**Governance chain:** ZivaID → ZivaLatam → BHG
**Supreme internal authority:** BHG Constitution
**Phase:** Post-conceptual-verification / Pre-market-validation
**Verification record:** `ZIVAID_POST_MERGE_VERIFICATION_R00.md`

## 0. Governance, authority and non-override rule

ZivaID is a product of ZivaLatam. ZivaID therefore operates under the governance, standards, policies and directives legitimately established by ZivaLatam.

ZivaLatam operates within the governance authority of Breto's Holding Group (BHG). ZivaLatam-level rules, product rules and future subsidiary-level rules may not contradict the BHG Constitution or applicable higher-order BHG governance instruments.

The internal ascending authority chain is:

```text
ZivaID
  ↑
ZivaLatam
  ↑
Breto's Holding Group (BHG)
  ↑
BHG Constitution — supreme internal governing authority
```

This is the product's internal organizational authority chain. Applicable law, regulation, court orders and other binding external obligations remain superior to internal corporate governance and cannot be overridden by ZivaID, ZivaLatam or BHG product documentation.

### Authority rule

No ZivaID:

- product requirement;
- policy;
- technical design;
- API contract;
- data rule;
- authorization rule;
- credential rule;
- operational procedure;
- future subsidiary integration;

may be interpreted as authority to weaken, bypass, contradict or silently alter a valid higher-level BHG or ZivaLatam directive.

Where a conflict is identified, the conflict must be escalated to the appropriate higher governance layer and resolved through an explicit, traceable governance decision. Product documentation and engineering implementation must not silently resolve an authority conflict in favor of the lower layer.

### Governance inheritance

ZivaID inherits applicable constraints from ZivaLatam and, through ZivaLatam, from BHG. A future ZivaID version may add product-specific rules, but those rules are subordinate rules and cannot supersede higher-authority governance.

This relationship must be preserved throughout product evolution.

## 1. Product identity and corporate hierarchy

ZivaID is a product of ZivaLatam. It is not regionalized into separate products such as "ZivaID Chile", "ZivaID Perú" or "ZivaID Colombia".

The conceptual hierarchy is:

```text
Breto's Holding Group (BHG)
└── Ziva / ZivaLatam
    ├── ZivaID
    ├── ZivaPay
    ├── ZivaOS
    └── future products and services
```

Jurisdictional operations are a property of ZivaLatam's legal and operational structure, not separate ZivaID products.

## 2. Product purpose

ZivaID is an interoperable identity and trust infrastructure intended to provide a reusable identity layer for ZivaLatam products and, where supported, external compatible services.

It can provide authentication, credential presentation, verification, authorization and evidence without turning authentication into universal data access.

Core principle:

> One ZivaID, multiple services — without universal data access.

## 3. Universal login / identity provider

ZivaID is intended to operate as the identity provider for compatible ZivaLatam products and may support compatible external services where appropriate.

A user may authenticate to ZivaPay, ZivaOS and future services through ZivaID instead of maintaining a separate identity for each product.

Conceptual flow:

```text
User
  ↓
Continue with ZivaID
  ↓
ZivaID authentication
  ↓
Service identity established
  ↓
Service requests only required credentials
  ↓
ZivaID evaluates authorization/policy
  ↓
Only permitted information is presented
```

Authentication establishes identity. It does not automatically authorize access to every domain or credential.

## 4. Credential reusability

A compatible service should be able to reuse a valid, relevant credential instead of repeatedly asking the user to submit the same evidence, provided that:

- the credential remains valid;
- the issuer is trusted for the required purpose;
- the intended purpose is compatible;
- the user and/or other lawful authorization requirements are satisfied;
- applicable regulation permits reuse;
- any required freshness or re-verification requirement is met.

This creates the possibility of reducing redundant onboarding and recertification.

"Zero re-KYC" is a market and regulatory hypothesis, not a universal product promise.

## 5. Service-scoped authorization

Every authorized service may request credentials required for its own purpose. ZivaID determines what may be presented according to policy, context, purpose, authorization, jurisdiction and other applicable controls.

Example:

```text
ZivaPay → requests financial/KYC credentials for an authorized financial purpose
ZivaOS  → requests only credentials needed by the OS/service context
Pharmacy → requests prescription credentials needed for dispensing
Hospital → may request clinically relevant health information when authorized
```

A service receives an authorized presentation, not an unrestricted copy of the user's identity.

## 6. Separation of authentication and authorization

### Authentication

> Who is this participant?

### Authorization

> What may this service access or verify in this context?

These must remain separate architectural concepts.

## 7. Policy evaluation

ZivaID should investigate a policy engine capable of evaluating requests using factors such as:

```text
Requester
Subject
Credential
Domain
Purpose
Legal basis / authority
Scope
Time validity
Jurisdiction
Credential status
Trust level
```

The result should be an explicit allow, deny or controlled outcome.

## 8. Identity domains

Potential domains remain:

- Foundational identity
- Legal identity
- Migration status
- Financial profile
- Health identity
- Academic identity
- Employment identity
- Housing profile
- Business identity

Domains are separated by policy. A credential's existence does not grant cross-domain access.

## 9. Data sovereignty and non-appropriation

ZivaID, ZivaLatam and BHG do not acquire ownership of participant information merely because they provide identity, credential, verification, storage, transport or interoperability services.

Applicable rights, custody, obligations and restrictions remain determined by the information type, participant roles, legal relationships and applicable law.

The conceptual model treats participants as retaining the rights and control applicable to their information; it does not assume that ZivaID, ZivaLatam or BHG become owners merely by operating the infrastructure.

## 10. Portability

Portability does not mean moving from "ZivaID Chile" to "ZivaID Perú", because those are not separate products.

Instead, legitimate portable data and credentials should be capable of being used across compatible ZivaLatam operations and compatible external infrastructure, subject to jurisdictional requirements.

Conceptually:

```text
ZivaID
  ↓ portable credentials / data
ZivaLatam Chile
  ↓
ZivaLatam Perú
  ↓
ZivaLatam Colombia
  ↓
compatible external infrastructure
```

The identity product remains ZivaID. Jurisdictional legal entities and regulatory environments may differ.

Portability does not override data-localization, sector-specific retention, evidentiary, regulatory or other legal requirements.

## 11. Person and business identity

ZivaID must conceptually support both individual and organizational identities.

It should support verifiable relationships such as:

- person ↔ organization;
- organization ↔ person;
- organization ↔ organization;
- representative ↔ company;
- employee ↔ employer;
- professional ↔ institution.

## 12. Progressive trust

ZivaID should investigate a trust model based on verifiable evidence rather than a generic assertion that a person or organization is "trusted".

Potential dimensions include:

- source authority;
- verification strength;
- credential freshness;
- credential status;
- issuer reputation;
- provenance;
- number and quality of corroborating credentials.

A future service may establish different evidence thresholds for different services or transaction levels.

## 13. Financial example

A future ZivaPay service could request already verified credentials needed for onboarding or credit assessment instead of repeatedly collecting the same documents.

Conceptually:

```text
ZivaID
  ├── identity credential
  ├── residence credential
  ├── migration credential
  ├── employment credential
  └── financial credentials
          ↓
       ZivaPay
          ↓
  service-specific evaluation
          ↓
   decision / offer
```

ZivaID provides evidence and credentials. ZivaPay remains responsible for its own financial evaluation, eligibility rules and regulatory obligations.

The existence of credentials does not guarantee credit approval.

## 14. Health example

A hospital may request clinically relevant health information when authorized. A pharmacy may request only the prescription credential required for dispensing.

A pharmacy should not automatically receive the user's complete medical history merely because the prescription is associated with the same ZivaID.

Potential vaccination proofs may use derived attributes such as "requirement satisfied" without exposing unnecessary clinical detail.

Health use cases require separate legal, regulatory, security and clinical validation before implementation.

## 15. Minimum disclosure

ZivaID should favor derived proofs and attribute-level responses where they satisfy the service's legitimate need.

Example:

```text
Requirement: user must be over 18
Response: ELIGIBLE
```

rather than automatically disclosing the full birth date and identity document.

## 16. Consent and temporary permissions

Consent should be contextual and, where appropriate, granular. Permissions may be limited by purpose, scope and duration.

A consent mechanism cannot override a legal or policy prohibition.

Permissions should support expiration and revocation where applicable.

Consent is one possible authorization mechanism; it is not necessarily the sole legal or technical basis for every permitted access.

## 17. Auditability

Relevant access events should be traceable to:

- requester;
- subject;
- requested credential/data;
- purpose;
- authorization;
- timestamp;
- outcome;
- information actually disclosed;
- credential/source supporting the decision.

## 18. Non-surveillance

ZivaID must not be designed as a universal surveillance mechanism. Cross-domain correlation, profiling and tracking must require legitimate authority and appropriate controls.

## 19. BHG / ZivaLatam dogfooding

BHG and ZivaLatam should use the same principles internally where appropriate. Publicly appropriate governance, corporate and verification information should be made auditable, while personal, confidential, security-sensitive and legally restricted information remains protected.

Principle:

> Maximum legitimate transparency; maximum legitimate protection.

## 20. Anti-lock-in

The value of ZivaID should derive from trust, interoperability, usability, standards, security, verification and network effects rather than preventing users or organizations from leaving.

## 21. Scope boundary

This version remains conceptual. It is not a final legal framework, privacy policy, technical architecture, API specification, database schema, regulatory approval, production implementation or authorization to process real sensitive information.

## 22. Market hypothesis

The central hypothesis is that people and organizations have meaningful demand for reusable, interoperable identity and credentials that reduce repetitive verification and onboarding while preserving contextual access, data sovereignty and portability.

The hypothesis must be tested rather than assumed true.

## 23. Version relationship

v0.2 is an explicit evolution of the historical v0.1 baseline. v0.1 is preserved as the historical conceptual baseline and the material evolution is recorded in `ZIVAID_VERSION_HISTORY.md`.

## 24. Next phase

The next authorized phase is **ZivaID Market Validation R00**.

No production engineering should begin solely because this document exists.

## 25. Governance continuity and change-control rule

The authority relationship defined in Section 0 is itself a controlled governance constraint:

> **ZivaID → ZivaLatam → BHG → BHG Constitution**

Future ZivaID versions may refine product behavior, but may not weaken, bypass or reinterpret higher-level authority through product documentation alone. Any proposed change affecting governance boundaries, delegation, authority, or the relationship between ZivaID and ZivaLatam/BHG requires explicit governance review and traceable approval at the appropriate higher layer before it becomes a product rule.

A technical implementation that conflicts with a higher-level governance requirement is non-conforming even if the implementation is technically functional.

## 26. Verification and merge record

v0.2 completed the independent second-round verification associated with PR #2. The PR was approved and merged into `main` as merge commit `aa7a89e6dd7015e9972e0955a0209eb812fc59e9`.

This verification establishes documentary and governance baseline status only. It does not constitute legal, regulatory, security, clinical, financial or market certification.
