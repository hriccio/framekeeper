# Request Slice Map

- Change: `0020`
- Request: `work/changes/0020/request.md`
- Status: accepted

## Request Boundary

Add five pages that keep source currency and reference freshness explicit.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0080-sources-need-refresh-cycles.md` | accepted | Adds an episode page about sources needing refresh cycles. | `tests/integration/test_knowledge_layer_next_five_pages_batch_sixteen.py` |
| `docs/slices/0081-policy-references-age-over-time.md` | accepted | Adds an episode page about policy references aging over time. | `tests/integration/test_knowledge_layer_next_five_pages_batch_sixteen.py` |
| `docs/slices/0082-source-currency-keeps-trust-intact.md` | accepted | Adds a concept page about source currency keeping trust intact. | `tests/integration/test_knowledge_layer_next_five_pages_batch_sixteen.py` |
| `docs/slices/0083-reference-drift-needs-review.md` | accepted | Adds a concept page about reference drift needing review. | `tests/integration/test_knowledge_layer_next_five_pages_batch_sixteen.py` |
| `docs/slices/0084-reference-refresh-workflow.md` | accepted | Adds a note page describing the reference refresh workflow. | `tests/integration/test_knowledge_layer_next_five_pages_batch_sixteen.py` |

## Out Of Scope

- automation and generation
- publishing infrastructure
- search and database support

## Open Questions

- none for this slice batch

## EGD Notes

Expectation-gap review should verify that external sources are treated as
versioned, time-sensitive evidence rather than static truth.
