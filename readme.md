# Framekeeper

Framekeeper is a low-friction video processing and classification tool for the
`@umoutrohenrique` content pipeline.

It exists to assist with mechanical processing:

- ingest raw videos
- transcribe spoken content
- classify YouTube policy risk
- produce non-blocking signal feedback
- prepare structured artifacts for a public knowledge layer

It must not decide meaning, optimize for algorithmic performance, or replace
human publication judgment.

## Governing Boundary

Automation handles mechanics.

Henrique handles meaning.

The only automated stage allowed to block a video is the safety gate. Signal
feedback is diagnostic only and must never block publication.

## Initial Sources

Original handoff material is preserved under:

- `work/sources/initial_handoff/um_outro_henrique-content_automation_system-context.md`
- `work/sources/initial_handoff/github-pages-knowledge-layer-codex-handoff.md`

Start extraction from those files, then refine the model into repository
artifacts before implementing code.

## Initial Workflow

The intended content flow is:

```text
raw video -> transcript -> safety gate -> signal feedback -> release packet
```

The related knowledge-layer flow is:

```text
video -> transcript -> extract ideas -> enrich references -> publish markdown/site content
```

Framekeeper should support both flows without coupling video processing to
public publishing.

## MRL Usage

This repository was created from `wastingnotime/mrl-starter`.

Read these files before substantial work:

- `AGENTS.md`
- `docs/operating/mrl_reference.md`
- `docs/operating/skills_workflow.md`
- `docs/semantics/model_hypothesis.md`
- `docs/semantics/domain_background_knowledge.md`
- `docs/slices/0001-video-processing-classification.md`

Recommended next phase: run `extract` from the initial handoff sources, then
run `refine` for the first minimal slice.
