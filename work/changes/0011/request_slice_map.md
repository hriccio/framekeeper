# Request Slice Map

- Change: `0011`
- Request: `work/changes/0011/request.md`
- Status: accepted

## Request Boundary

Add five pages that describe versioning, archival, and accountability for older
content.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0035-older-pages-still-matter.md` | accepted | Adds an episode page about older pages still mattering. | `tests/integration/test_knowledge_layer_next_five_pages_batch_seven.py` |
| `docs/slices/0036-archives-are-readable.md` | accepted | Adds an episode page about archives remaining readable. | `tests/integration/test_knowledge_layer_next_five_pages_batch_seven.py` |
| `docs/slices/0037-version-history-is-visible.md` | accepted | Adds a concept page about version history being visible. | `tests/integration/test_knowledge_layer_next_five_pages_batch_seven.py` |
| `docs/slices/0038-archival-pages-stay-linked.md` | accepted | Adds a concept page about archival pages staying linked. | `tests/integration/test_knowledge_layer_next_five_pages_batch_seven.py` |
| `docs/slices/0039-archive-maintenance-workflow.md` | accepted | Adds a note page describing the archive maintenance workflow. | `tests/integration/test_knowledge_layer_next_five_pages_batch_seven.py` |

## Out Of Scope

- automation and generation
- publishing infrastructure
- search and database support

## Open Questions

- none for this slice batch

## EGD Notes

Expectation-gap review should verify that archival behavior stays readable and
accountable without turning the site into a change log.

