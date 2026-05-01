# Request Slice Map

- Change: `0008`
- Request: `work/changes/0008/request.md`
- Status: accepted

## Request Boundary

Add five pages that document the site's maintenance rules and editing shape.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0020-episodes-should-stay-short.md` | accepted | Adds an episode page about keeping episode pages short. | `tests/integration/test_knowledge_layer_next_five_pages_batch_four.py` |
| `docs/slices/0021-concepts-point-to-episodes.md` | accepted | Adds an episode page about concept pages pointing back to episodes. | `tests/integration/test_knowledge_layer_next_five_pages_batch_four.py` |
| `docs/slices/0022-local-links-make-the-site-relatable.md` | accepted | Adds a concept page about local links keeping the site easy to browse. | `tests/integration/test_knowledge_layer_next_five_pages_batch_four.py` |
| `docs/slices/0023-source-discipline-keeps-content-honest.md` | accepted | Adds a concept page about keeping source discipline strict. | `tests/integration/test_knowledge_layer_next_five_pages_batch_four.py` |
| `docs/slices/0024-adding-new-pages-workflow.md` | accepted | Adds a note page describing the workflow for adding new pages. | `tests/integration/test_knowledge_layer_next_five_pages_batch_four.py` |

## Out Of Scope

- automation and generation
- publishing infrastructure
- search and database support

## Open Questions

- none for this slice batch

## EGD Notes

Expectation-gap review should verify that the pages reduce maintenance friction
without adding unnecessary process clutter.

