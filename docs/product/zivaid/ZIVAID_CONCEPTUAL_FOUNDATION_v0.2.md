# ZivaID — Conceptual Foundation v0.2

**Status:** Current conceptual baseline pending independent verification
**Version:** 0.2
**Product:** ZivaID
**Brand / ecosystem:** Ziva / ZivaLatam
**Operating legal entities:** ZivaLatam [jurisdiction] SpA, when a jurisdiction-specific legal entity must be distinguished
**Holding:** Breto's Holding Group (BHG)
**Phase:** Pre-market-validation / Pre-engineering

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

ZivaID may operate as the identity provider for compatible ZivaLatam products.

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

The identity product remains ZivaID. Jurisdictional entities and regulatory environments may differ.

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

This version is still conceptual. It is not a final legal framework, privacy policy, technical architecture, API specification, database schema, regulatory approval, production implementation or authorization to process real sensitive information.

## 22. Market hypothesis

The central hypothesis is that people and organizations have meaningful demand for reusable, interoperable identity and credentials that reduce repetitive verification and onboarding while preserving contextual access, data sovereignty and portability.

The hypothesis must be tested rather than assumed true.

## 23. Version relationship

v0.2 is an explicit evolution of the historical v0.1 baseline. v0.1 is preserved unchanged for traceability. Material differences are recorded in `ZIVAID_VERSION_HISTORY.md`.

## 24. Next phase

The next authorized phase after independent verification of this conceptual baseline is **ZivaID Market Validation R00**.

No production engineering should begin solely because this document exists.
