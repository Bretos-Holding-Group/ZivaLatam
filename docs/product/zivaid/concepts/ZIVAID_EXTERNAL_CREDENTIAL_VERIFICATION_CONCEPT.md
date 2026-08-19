# ZivaID — External Credential Verification Concept

**Status:** PROPOSED
**Type:** Concept / Architectural Proposal
**Authority:** Non-authoritative
**Product:** ZivaID
**Domain:** Identity, credentials and verification
**Origin:** External regulatory reference
**Initial reference case:** SERMIG — Habilitación Laboral (Chile)
**Related baseline:** `ZIVAID_CONCEPTUAL_FOUNDATION_v0.2.md`

## 1. Purpose

This document records a proposed ZivaID capability for processing, verifying, correlating and presenting credentials or assertions issued by external authorities and other legitimate issuers.

It is a concept only. It does not create product authority, regulatory authority, legal status, certification authority, or production authorization.

## 2. Core authority boundary

ZivaID must never become the authority that originates, grants, modifies, suspends or revokes an external credential, authorization or legal status.

The issuer remains the authority for the assertion it issues.

Conceptual relationship:

```text
External Authority / Issuer
        ↓
Credential / Assertion
        ↓
Evidence
        ↓
ZivaID verification and provenance processing
        ↓
ZivaID presentation / status representation
```

ZivaID may process evidence and assertions according to applicable rules, but it must not represent its own verification as the source of the underlying authorization.

## 3. Initial reference case — SERMIG Habilitación Laboral

SERMIG announced the Habilitación Laboral procedure in August 2026. The official service describes it as a certificate that allows verification of whether a foreign person is authorized to perform remunerated activities in Chile.

This is recorded as a reference case for architectural exploration, not as a ZivaID dependency or product requirement.

The authoritative source remains SERMIG and the applicable Chilean legal and regulatory framework.

## 4. Progressive verification model

The capability may evolve through controlled stages:

```text
Manual evidence submission
        ↓
Assisted verification
        ↓
Automated document / QR / pattern verification
        ↓
Official-source integration where legitimately available
        ↓
Continuous or event-driven status verification where supported
```

Automation must not change the authority boundary. A technically automated verification remains a verification of an issuer's assertion, not an authorization created by ZivaID.

## 5. Conceptual credential attributes

A future implementation may need to represent attributes such as:

- issuer;
- subject;
- credential or assertion type;
- jurisdiction;
- issuance date;
- validity period;
- status;
- scope;
- restrictions;
- verification method;
- evidence reference;
- provenance;
- verification timestamp;
- source confidence or verification strength.

These attributes are exploratory and are not a finalized data model.

## 6. Verification and provenance

ZivaID should preserve enough provenance to distinguish:

- what the issuer asserted;
- what evidence the user supplied;
- how the evidence was verified;
- when the verification occurred;
- which source or mechanism was used;
- what status was observed;
- what ZivaID actually concluded from the evidence.

The system must not collapse these layers into a single undifferentiated "verified" flag.

## 7. External authority examples

The model is intended to remain issuer-agnostic. Potential issuer categories may include government authorities, educational institutions, employers, regulated financial institutions, professional bodies and other legitimate organizations.

SERMIG is the initial reference case because the Habilitación Laboral service provides a concrete example of an externally issued, verifiable authorization-related credential.

## 8. Product boundary

ZivaID may conceptually:

- receive evidence from a user;
- inspect document structure and machine-readable elements;
- verify available patterns or signatures;
- correlate evidence with an issuer assertion when legitimately possible;
- retain provenance and verification history;
- present a credential or derived attribute to an authorized service.

ZivaID may not, by virtue of this capability:

- grant work authorization;
- certify legal status independently of the issuer;
- replace an issuing authority;
- manufacture an official certificate;
- revoke an issuer's credential;
- represent an internal ZivaID result as an official government determination.

## 9. Progressive trust

Future verification strength may depend on the provenance and verification method available. A user-submitted document, an internally checked QR code and a directly verified official source should not necessarily be treated as equivalent evidence.

Any future trust model must remain explicit, auditable and context-specific.

## 10. Governance and change control

This proposal is subordinate to the current ZivaID conceptual baseline and to the ZivaLatam/BHG governance hierarchy.

Any future change that affects governance boundaries, regulatory positioning, authority delegation, handling of sensitive information, or the relationship between ZivaID and an external authority requires the appropriate governance review before becoming effective product policy or implementation.

No production engineering is authorized solely by this document.

## 11. Open questions

Before implementation, ZivaID should determine:

1. Which credential types provide sufficient legal and technical evidence for each use case?
2. How should issuer trust and verification strength be represented?
3. How should expiration, revocation and supersession be handled?
4. Which official verification mechanisms may legitimately be integrated?
5. What user authorization and privacy controls apply to each credential presentation?
6. Which evidence must be retained, for how long, and under what jurisdictional rules?
7. How should conflicting or stale evidence be represented?

## 12. Non-authoritative status

This document is a proposal for future architectural investigation. It is not a standard, policy, legal interpretation, regulatory certification, API specification, database schema or implementation authorization.

The underlying external authority remains responsible for the validity and legal effect of its own credentials and determinations.
