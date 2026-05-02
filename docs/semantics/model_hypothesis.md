# Model Hypothesis

## Purpose

Framekeeper models a video intake pipeline where automation supports mechanical
processing and classification while preserving human authority over meaning and
publication.

This document is the initial hypothesis. Treat it as input for the first
`extract` and `refine` phases, not as final domain truth.

## Governing Sentence

Automation handles mechanics; Henrique handles meaning.

## Core Boundary

Framekeeper separates three concerns:

- processing: turn raw video into transcript and derived metadata
- safety: classify hard policy risk and block only when necessary
- signal: provide soft feedback that can improve clarity without controlling output

Safety and signal must never be mixed.

## Candidate Concepts

- `Video`: a recorded source file awaiting processing.
- `Transcript`: text extracted from a video.
- `ProcessingRun`: one attempt to process a video through automated stages.
- `SafetyGate`: hard classifier for YouTube policy risk.
- `RiskLevel`: `SAFE`, `REVIEW`, or `BLOCK`.
- `SignalFeedback`: non-blocking summary, audience, hook, and diagnostic scores.
- `ReleasePacket`: human-readable output prepared for manual publication review.
- `KnowledgeArtifact`: markdown-oriented output for the slower public knowledge layer.
- `MarkdownDraft`: a local draft artifact produced from transcript extraction and
  reference enrichment before site publication.

## Candidate Use Cases

- register a raw video for processing
- transcribe a video
- classify safety risk from transcript, title, and metadata
- generate non-blocking signal feedback
- produce a release packet for manual review
- create a draft episode artifact from a transcript
- update reusable concept and reference candidates
- generate markdown draft content from a transcript with local model-backed
  extraction and enrichment

## Initial State Flow

```text
raw -> transcribed -> safety_checked -> feedback_generated -> ready_for_review
```

Blocking path:

```text
safety_checked -> blocked
```

Manual path:

```text
ready_for_review -> approved_by_henrique -> published_outside_framekeeper
```

Framekeeper should record publication intent or result only when useful, but it
must not publish automatically in the first slice.

## Hard Rules

- only the safety gate can block a video
- signal feedback must never block or suppress a video
- heuristic scores are diagnostic only
- no algorithmic performance optimization
- no generic "quality gate"
- preserve raw evidence before deriving refined artifacts
- keep raw transcripts out of a public site unless intentionally exposed
- markdown draft generation is an intermediate knowledge-layer step, not
  publication itself

## Open Questions

- Should the first implementation use local Whisper, an API transcription path,
  or a replaceable transcript port with a fake adapter?
- Should storage start as filesystem-only, SQLite, or both?
- Should `RiskLevel.BLOCK` require explicit human override support from day one?
- Should knowledge-layer draft generation live in Framekeeper immediately or be
  a later integration boundary?
- Should the project remain Python-first through the starter pack, or switch to
  another pack before code begins?
