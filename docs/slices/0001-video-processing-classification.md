# Slice 0001 - Video Processing Classification

## Status

Proposed.

## Intent

Create the smallest useful Framekeeper workflow:

```text
registered video + transcript -> safety classification -> signal feedback -> release packet
```

This slice should make the core boundary executable without requiring real video
transcription, real YouTube publishing, or a public knowledge site.

## In Scope

- define the domain vocabulary for videos, transcripts, safety risk, and signal feedback
- implement or sketch a deterministic local path for classifying one transcript
- produce a release packet that a human can inspect
- keep safety and signal outputs structurally separate
- add tests that prove `BLOCK` stops the pipeline and signal never blocks

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

## First Extraction Inputs

- `work/sources/initial_handoff/um_outro_henrique-content_automation_system-context.md`
- `work/sources/initial_handoff/github-pages-knowledge-layer-codex-handoff.md`

## Open Design Decisions

- whether to keep the default `python_ddd_monolith` pack
- whether first storage should be filesystem-only or SQLite
- whether a release packet should be Markdown, JSON, or both
- whether knowledge-layer draft generation belongs in this first slice
