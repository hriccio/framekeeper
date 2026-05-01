# Request Slice Map

- Change: `0010`
- Request: `work/changes/0010/request.md`
- Status: accepted

## Request Boundary

Add five pages that preserve the site's page shape, metadata use, and index
discipline.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0030-metadata-keeps-pages-readable.md` | accepted | Adds an episode page about metadata making pages readable. | `tests/integration/test_knowledge_layer_next_five_pages_batch_six.py` |
| `docs/slices/0031-template-pages-prevent-drift.md` | accepted | Adds an episode page about templates preventing drift. | `tests/integration/test_knowledge_layer_next_five_pages_batch_six.py` |
| `docs/slices/0032-page-shape-should-stay-predictable.md` | accepted | Adds a concept page about predictable page shape. | `tests/integration/test_knowledge_layer_next_five_pages_batch_six.py` |
| `docs/slices/0033-indices-are-part-of-the-content-model.md` | accepted | Adds a concept page about indices being part of the content model. | `tests/integration/test_knowledge_layer_next_five_pages_batch_six.py` |
| `docs/slices/0034-synchronizing-page-numbers.md` | accepted | Adds a note page about keeping page numbers and indices in sync. | `tests/integration/test_knowledge_layer_next_five_pages_batch_six.py` |

## Out Of Scope

- automation and generation
- publishing infrastructure
- search and database support

## Open Questions

- none for this slice batch

## EGD Notes

Expectation-gap review should verify that the new pages support maintainable
page shape without turning into site-generator or repo-operations guidance.

