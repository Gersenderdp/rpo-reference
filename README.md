# OpenProof — RPO Reference Implementation
Reference implementation for the Registered Probative Object (RPO).

OpenProof introduces a deterministic evidential bundle designed to make institutional decisions defensible under scrutiny.

Same input → same sealed bundle → same hash.
Any modification → detectable.

Specification

The RPO specification is defined here:
https://github.com/Gersenderdp/rpo-spec-v0.1


Example bundle -> example-bundle.json demonstrates the minimal structure of a Registered Probative Object.

validator.py verifies bundle integrity and hash consistency.
