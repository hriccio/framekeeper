# Request Slice Map

- Change: `0012`
- Request: `work/changes/0012/request.md`
- Status: accepted

## Request Boundary

Add five pages that document the jobs of the site's content families.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0040-content-families-keep-the-site-structured.md` | accepted | Adds an episode page about content families keeping the site structured. | `tests/integration/test_knowledge_layer_next_five_pages_batch_eight.py` |
| `docs/slices/0041-notes-are-for-intermediate-thinking.md` | accepted | Adds an episode page about notes as intermediate thinking. | `tests/integration/test_knowledge_layer_next_five_pages_batch_eight.py` |
| `docs/slices/0042-page-families-have-different-jobs.md` | accepted | Adds a concept page about page families having different jobs. | `tests/integration/test_knowledge_layer_next_five_pages_batch_eight.py` |
| `docs/slices/0043-reference-pages-need-scope.md` | accepted | Adds a concept page about reference pages needing scope. | `tests/integration/test_knowledge_layer_next_five_pages_batch_eight.py` |
| `docs/slices/0044-page-family-map.md` | accepted | Adds a note page describing the page family map. | `tests/integration/test_knowledge_layer_next_five_pages_batch_eight.py` |

## Out Of Scope

- automation and generation
- publishing infrastructure
- search and database support

## Open Questions

- none for this slice batch

## EGD Notes

Expectation-gap review should verify that the page families remain distinct and
that the new pages do not collapse their different roles into one generic
content type.

