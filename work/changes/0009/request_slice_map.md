# Request Slice Map

- Change: `0009`
- Request: `work/changes/0009/request.md`
- Status: accepted

## Request Boundary

Add five pages that explain how content moves from draft to refined form.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0025-drafts-become-refined-pages.md` | accepted | Adds an episode page about drafts becoming refined pages. | `tests/integration/test_knowledge_layer_next_five_pages_batch_five.py` |
| `docs/slices/0026-review-before-publishing.md` | accepted | Adds an episode page about reviewing before publishing. | `tests/integration/test_knowledge_layer_next_five_pages_batch_five.py` |
| `docs/slices/0027-drafts-are-not-final.md` | accepted | Adds a concept page about drafts not being final content. | `tests/integration/test_knowledge_layer_next_five_pages_batch_five.py` |
| `docs/slices/0028-review-preserves-context.md` | accepted | Adds a concept page about review preserving context and intent. | `tests/integration/test_knowledge_layer_next_five_pages_batch_five.py` |
| `docs/slices/0029-draft-to-refined-workflow.md` | accepted | Adds a note page describing the draft-to-refined workflow. | `tests/integration/test_knowledge_layer_next_five_pages_batch_five.py` |

## Out Of Scope

- automation and generation
- publishing infrastructure
- search and database support

## Open Questions

- none for this slice batch

## EGD Notes

Expectation-gap review should verify that draft handling is explicit and that
the pages preserve the separation between intermediate and published material.

