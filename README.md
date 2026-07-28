# OpenProof — RPO Reference Implementation

> **OpenProof is the probative infrastructure. TruthX Engine is the deterministic structuring engine powering it. RPO is the Registered Probative Object it produces.**

This repository provides a public reference implementation of the **Registered Probative Object (RPO)** specification.

It shows how fragmented evidence can be represented as a structured, traceable and machine-verifiable record for human review.

## Role in the architecture

| Component | Role |
|---|---|
| **TruthX Engine** | Structures heterogeneous evidence through a controlled, deterministic pipeline. |
| **RPO** | Preserves the resulting record, its sources, transformations, reservations and integrity data. |
| **OpenProof** | Provides the probative infrastructure and verification layer. |

**Processing chain:**

`Evidence → TruthX Engine → RPO → OpenProof validation`

## What this repository demonstrates

The reference implementation illustrates:

- the minimum structure of an RPO bundle;
- deterministic serialization of the record;
- generation of a reproducible integrity hash;
- detection of subsequent modifications;
- separation between machine-verifiable data and human-readable content.

The file [`example-bundle.json`](example-bundle.json) provides a minimal example.

## Deterministic integrity

For the same normalized input, a compliant implementation must produce the same sealed representation and the same integrity hash.

Any later modification to the protected content must be detectable.

## Official specification

The canonical public RPO specification is maintained here:

[openproof-net/rpo-spec-v0.1](https://github.com/openproof-net/rpo-spec-v0.1)

This repository implements and illustrates that specification. It does not replace it.

## Scope and limits

This reference implementation can verify structural conformity and integrity.

It does **not**:

- determine whether an allegation is true;
- assess the legal weight of evidence;
- replace expert analysis or human judgment;
- make institutional, judicial or governance decisions.

**Automation supports judgment. It does not replace authority or accountability.**

## Related repositories

- [RPO Specification](https://github.com/openproof-net/rpo-spec-v0.1) — canonical public specification.
- [RPO Examples](https://github.com/Gersenderdp/rpo-examples) — example probative objects and use cases.
- [OpenProof Validator](https://github.com/Gersenderdp/openproof-validator) — conformity and integrity validation tools.

## Maintainer

Maintained by [Gersende de Parcey](https://github.com/Gersenderdp), founder of TruthX and builder of OpenProof.
