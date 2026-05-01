# Request Slice Map

- Change: `0017`
- Request: `work/changes/0017/request.md`
- Status: accepted

## Request Boundary

Add five pages that keep transcript material private and public pages refined.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0065-raw-transcripts-stay-private.md` | accepted | Adds an episode page about raw transcripts staying private. | `tests/integration/test_knowledge_layer_next_five_pages_batch_thirteen.py` |
| `docs/slices/0066-public-pages-are-refined.md` | accepted | Adds an episode page about public pages staying refined. | `tests/integration/test_knowledge_layer_next_five_pages_batch_thirteen.py` |
| `docs/slices/0067-raw-evidence-is-not-the-site.md` | accepted | Adds a concept page about raw evidence not becoming the public site. | `tests/integration/test_knowledge_layer_next_five_pages_batch_thirteen.py` |
| `docs/slices/0068-public-content-needs-selection.md` | accepted | Adds a concept page about public content needing selection. | `tests/integration/test_knowledge_layer_next_five_pages_batch_thirteen.py` |
| `docs/slices/0069-transcript-to-public-workflow.md` | accepted | Adds a note page describing the transcript-to-public workflow. | `tests/integration/test_knowledge_layer_next_five_pages_batch_thirteen.py` |

## Out Of Scope

- automation and generation
- publishing infrastructure
- search and database support

## Open Questions

- none for this slice batch

## EGD Notes

Expectation-gap review should verify that raw transcript material remains a
private working input and that the public layer only receives refined content.
