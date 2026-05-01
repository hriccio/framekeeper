# Request Slice Map

- Change: `0026`
- Request: `work/changes/0026/request.md`
- Status: accepted

## Request Boundary

Add five pages that keep processing runs, transcripts, and metadata explicit.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0110-processing-runs-stay-inspectable.md` | accepted | Adds an episode page about processing runs staying inspectable. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentytwo.py` |
| `docs/slices/0111-transcripts-and-metadata-travel-together.md` | accepted | Adds an episode page about transcripts and metadata traveling together. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentytwo.py` |
| `docs/slices/0112-inspectable-runs-need-clear-artifacts.md` | accepted | Adds a concept page about inspectable runs needing clear artifacts. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentytwo.py` |
| `docs/slices/0113-transcripts-are-intermediate-artifacts.md` | accepted | Adds a concept page about transcripts being intermediate artifacts. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentytwo.py` |
| `docs/slices/0114-processing-run-workflow.md` | accepted | Adds a note page describing the processing run workflow. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentytwo.py` |

## Out Of Scope

- automation and generation
- publishing infrastructure
- search and database support

## Open Questions

- none for this slice batch

## EGD Notes

Expectation-gap review should verify that the processing run remains a
repeatable, inspectable step and not a hidden implementation detail.
