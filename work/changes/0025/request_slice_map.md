# Request Slice Map

- Change: `0025`
- Request: `work/changes/0025/request.md`
- Status: accepted

## Request Boundary

Add five pages that keep repository memory and loop history explicit.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0105-work-sources-hold-raw-evidence.md` | accepted | Adds an episode page about `work/sources` holding raw evidence. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentyone.py` |
| `docs/slices/0106-work-changes-preserve-loop-history.md` | accepted | Adds an episode page about `work/changes` preserving loop history. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentyone.py` |
| `docs/slices/0107-memory-is-split-by-purpose.md` | accepted | Adds a concept page about memory being split by purpose. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentyone.py` |
| `docs/slices/0108-change-artifacts-keep-the-loop-readable.md` | accepted | Adds a concept page about change artifacts keeping the loop readable. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentyone.py` |
| `docs/slices/0109-repository-memory-workflow.md` | accepted | Adds a note page describing the repository memory workflow. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentyone.py` |

## Out Of Scope

- automation and generation
- publishing infrastructure
- search and database support

## Open Questions

- none for this slice batch

## EGD Notes

Expectation-gap review should verify that raw evidence stays in `work/sources`
and that loop history is preserved through `work/changes`.
