# Request Slice Map

- Change: `0018`
- Request: `work/changes/0018/request.md`
- Status: accepted

## Request Boundary

Add five pages that keep idea extraction and draft shaping explicit.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0070-ideas-are-extracted-from-videos.md` | accepted | Adds an episode page about extracting ideas from videos. | `tests/integration/test_knowledge_layer_next_five_pages_batch_fourteen.py` |
| `docs/slices/0071-draft-pages-start-as-working-notes.md` | accepted | Adds an episode page about draft pages starting as working notes. | `tests/integration/test_knowledge_layer_next_five_pages_batch_fourteen.py` |
| `docs/slices/0072-extraction-turns-transcripts-into-candidates.md` | accepted | Adds a concept page about extraction creating candidates. | `tests/integration/test_knowledge_layer_next_five_pages_batch_fourteen.py` |
| `docs/slices/0073-draft-pages-need-editorial-shape.md` | accepted | Adds a concept page about draft pages needing editorial shape. | `tests/integration/test_knowledge_layer_next_five_pages_batch_fourteen.py` |
| `docs/slices/0074-idea-extraction-workflow.md` | accepted | Adds a note page describing the idea extraction workflow. | `tests/integration/test_knowledge_layer_next_five_pages_batch_fourteen.py` |

## Out Of Scope

- automation and generation
- publishing infrastructure
- search and database support

## Open Questions

- none for this slice batch

## EGD Notes

Expectation-gap review should verify that extraction creates reusable draft
material without collapsing the transcript and the final public pages into one
thing.
