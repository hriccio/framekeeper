# Request Slice Map

- Change: `0033`
- Request: `work/changes/0033/request.md`
- Status: accepted

## Request Boundary

Add one deterministic code slice that classifies transcript-derived ideas into
the knowledge-layer family they best fit.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0145-transcript-idea-family-classification.md` | accepted | Defines the code slice for transcript-idea family classification and the family-specific outcomes it should produce. | `tests/unit/test_classify_transcript_idea.py` |

## Out Of Scope

- automatic publishing
- workflow tracing artifacts
- knowledge-layer content generation
- safety-risk classification changes

## Open Questions

- none for this slice

## EGD Notes

Expectation-gap review should verify that the classifier helps route
transcript-derived ideas into the right content family without changing safety
behavior or turning into a publishing decision.
