# Request Slice Map

- Change: `0035`
- Request: `work/changes/0035/request.md`
- Status: accepted

## Request Boundary

Add a single runtime slice that turns a provided transcript into a markdown
draft for the knowledge layer by extracting ideas and enriching references
through local Llama-backed model calls.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0146-transcript-markdown-draft-generation.md` | proposed | Covers transcript-to-draft generation, including idea extraction, reference enrichment, and markdown rendering. | unit or integration tests for the draft-generation use case |

## Out Of Scope

- raw video ingestion
- broad flow orchestration outside Framekeeper
- GitHub Pages deployment
- automatic publication decisions

## Open Questions

- Should the slice generate one markdown draft per transcript or one draft per
  extracted idea?
- Should reference enrichment produce curated links only, or also source hints
  when the model cannot name a durable URL?

## EGD Notes

Expectation-gap review should verify that Framekeeper emits markdown drafts
only, with idea extraction preceding reference enrichment, and that the slice
remains local enough to test without a live model dependency.
