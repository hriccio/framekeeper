# Request Slice Map

- Change: `0031`
- Request: `work/changes/0031/request.md`
- Status: accepted

## Request Boundary

Add five pages that make request boundaries and slice maps explicit in the
public knowledge layer.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0135-requests-need-clear-boundaries.md` | accepted | Adds an episode page about requests needing clear boundaries. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentyseven.py` |
| `docs/slices/0136-slice-maps-make-coverage-visible.md` | accepted | Adds an episode page about slice maps making coverage visible. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentyseven.py` |
| `docs/slices/0137-requests-are-review-units.md` | accepted | Adds a concept page about requests being review units. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentyseven.py` |
| `docs/slices/0138-slice-docs-keep-build-bounded.md` | accepted | Adds a concept page about slice docs keeping build work bounded. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentyseven.py` |
| `docs/slices/0139-request-to-slice-workflow.md` | accepted | Adds a note page describing the request-to-slice workflow. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentyseven.py` |

## Out Of Scope

- automation and generation
- publishing infrastructure
- search and database support

## Open Questions

- none for this slice batch

## EGD Notes

Expectation-gap review should verify that requests remain the review boundary
and that slice maps are treated as traceability artifacts, not as implementation
specifications.
