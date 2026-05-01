# Request Slice Map

- Change: `0021`
- Request: `work/changes/0021/request.md`
- Status: accepted

## Request Boundary

Add five pages that keep overlap and pruning explicit in the knowledge layer.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0085-overlapping-ideas-need-pruning.md` | accepted | Adds an episode page about overlapping ideas needing pruning. | `tests/integration/test_knowledge_layer_next_five_pages_batch_seventeen.py` |
| `docs/slices/0086-pruned-pages-read-better.md` | accepted | Adds an episode page about pruned pages reading better. | `tests/integration/test_knowledge_layer_next_five_pages_batch_seventeen.py` |
| `docs/slices/0087-overlap-hurts-the-page-family-model.md` | accepted | Adds a concept page about overlap hurting the page-family model. | `tests/integration/test_knowledge_layer_next_five_pages_batch_seventeen.py` |
| `docs/slices/0088-pruning-keeps-the-site-focused.md` | accepted | Adds a concept page about pruning keeping the site focused. | `tests/integration/test_knowledge_layer_next_five_pages_batch_seventeen.py` |
| `docs/slices/0089-content-pruning-workflow.md` | accepted | Adds a note page describing the content pruning workflow. | `tests/integration/test_knowledge_layer_next_five_pages_batch_seventeen.py` |

## Out Of Scope

- automation and generation
- publishing infrastructure
- search and database support

## Open Questions

- none for this slice batch

## EGD Notes

Expectation-gap review should verify that pruning removes overlap without
collapsing distinct page families into one generic page.
