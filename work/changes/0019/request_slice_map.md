# Request Slice Map

- Change: `0019`
- Request: `work/changes/0019/request.md`
- Status: accepted

## Request Boundary

Add five pages that keep candidate promotion and page-family assignment explicit.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0075-candidate-ideas-need-a-family.md` | accepted | Adds an episode page about candidate ideas needing a family. | `tests/integration/test_knowledge_layer_next_five_pages_batch_fifteen.py` |
| `docs/slices/0076-references-become-reference-pages.md` | accepted | Adds an episode page about sources becoming reference pages. | `tests/integration/test_knowledge_layer_next_five_pages_batch_fifteen.py` |
| `docs/slices/0077-family-assignment-keeps-drafts-clear.md` | accepted | Adds a concept page about family assignment keeping drafts clear. | `tests/integration/test_knowledge_layer_next_five_pages_batch_fifteen.py` |
| `docs/slices/0078-draft-candidates-need-a-destination.md` | accepted | Adds a concept page about draft candidates needing a destination. | `tests/integration/test_knowledge_layer_next_five_pages_batch_fifteen.py` |
| `docs/slices/0079-candidate-promotion-workflow.md` | accepted | Adds a note page describing the candidate promotion workflow. | `tests/integration/test_knowledge_layer_next_five_pages_batch_fifteen.py` |

## Out Of Scope

- automation and generation
- publishing infrastructure
- search and database support

## Open Questions

- none for this slice batch

## EGD Notes

Expectation-gap review should verify that extracted candidates are assigned to
the correct page family before they are treated as draft pages.
