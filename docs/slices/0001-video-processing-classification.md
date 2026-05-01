# Slice 0001 - Video Processing Classification

## Status

Accepted.

## Selected Pack

- `python_ddd_monolith`

## Runtime Targets

- single Python runtime
- local deterministic execution for tests and scenario checks

## Architecture Mode

- DDD-inspired modular monolith
- thin application use case over deterministic domain components

## Intent

Create the smallest useful Framekeeper workflow:

```text
registered video + transcript -> safety classification -> signal feedback -> release packet
```

This slice should make the core boundary executable without requiring real video
transcription, real YouTube publishing, or a public knowledge site.

The built implementation uses transcript-only input for this first step. Raw
video ingestion, transcription services, and publishing remain outside the
slice.

## In Scope

- define the domain vocabulary for videos, transcripts, safety risk, and signal feedback
- implement or sketch a deterministic local path for classifying one transcript
- produce a release packet that a human can inspect
- keep safety and signal outputs structurally separate
- add tests that prove `BLOCK` stops the pipeline and signal never blocks

## Use-Case Contract

- input: registered video identifier, optional title, transcript, and optional
  metadata
- output: safety assessment, release packet, and optional signal feedback
- behavior: `BLOCK` prevents signal generation and marks the release packet as
  blocked
- behavior: `REVIEW` requires manual confirmation but still produces signal
  feedback
- behavior: `SAFE` produces a ready-for-review packet with signal feedback

## Main Business Rules

- safety is the hard gate
- signal is diagnostic only and must never alter the safety decision
- transcript input must be accepted without requiring a raw video file
- release packets must remain human-readable
- no storage layer is required for this first slice

## Required Ports

- none for this first slice
- future transcript, storage, or publishing integrations should be added as
  explicit ports when they become real requirements

## Out Of Scope

- automatic YouTube upload or publication
- GitHub Pages publishing
- production-grade Whisper integration
- real LLM provider integration without a port/fake boundary
- algorithmic performance optimization
- visual dashboard

## Candidate Acceptance Criteria

- a transcript can be processed without a raw video file
- safety output contains exactly one risk level: `SAFE`, `REVIEW`, or `BLOCK`
- `BLOCK` prevents creation of a ready-for-review release packet
- `REVIEW` produces a packet marked as requiring manual confirmation
- signal feedback is still produced or skipped according to an explicit rule,
  but it never changes the safety decision
- tests document the boundary between safety and signal

## Initial Test Plan

- safe transcript returns `SAFE` and a ready-for-review packet
- review transcript returns `REVIEW` and a manual-confirmation packet
- blocked transcript returns `BLOCK`, skips signal generation, and does not
  produce a ready-for-review packet

## Scenario Definition

1. submit a transcript about normal software work
2. submit a transcript with review-worthy wording
3. submit a transcript with blocked-risk wording

Each scenario should assert the safety result, packet status, and signal
behavior.

## Done Criteria

- the transcript-processing use case is implemented
- tests prove the safety and signal boundary
- the release packet can be inspected without reading internal objects
- the change is represented in `work/changes/0001/implementation.md`

## First Extraction Inputs

- `work/sources/initial_handoff/um_outro_henrique-content_automation_system-context.md`
- `work/sources/initial_handoff/github-pages-knowledge-layer-codex-handoff.md`

## Resolved Design Decisions

- keep the `python_ddd_monolith` pack for this first slice
- keep the first implementation in-process and state-free rather than adding
  storage
- produce a Markdown release packet for human inspection
- leave knowledge-layer draft generation for a later slice
