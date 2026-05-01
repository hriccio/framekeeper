# Request Slice Map

- Change: `0023`
- Request: `work/changes/0023/request.md`
- Status: accepted

## Request Boundary

Add five pages that keep safety review and blocking explicit.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0095-review-is-not-block.md` | accepted | Adds an episode page about review not being block. | `tests/integration/test_knowledge_layer_next_five_pages_batch_nineteen.py` |
| `docs/slices/0096-block-means-stop.md` | accepted | Adds an episode page about block meaning stop. | `tests/integration/test_knowledge_layer_next_five_pages_batch_nineteen.py` |
| `docs/slices/0097-review-and-block-are-distinct.md` | accepted | Adds a concept page about review and block being distinct. | `tests/integration/test_knowledge_layer_next_five_pages_batch_nineteen.py` |
| `docs/slices/0098-overrides-stay-explicit.md` | accepted | Adds a concept page about overrides staying explicit. | `tests/integration/test_knowledge_layer_next_five_pages_batch_nineteen.py` |
| `docs/slices/0099-safety-tier-workflow.md` | accepted | Adds a note page describing the safety tier workflow. | `tests/integration/test_knowledge_layer_next_five_pages_batch_nineteen.py` |

## Out Of Scope

- automation and generation
- publishing infrastructure
- search and database support

## Open Questions

- none for this slice batch

## EGD Notes

Expectation-gap review should verify that `REVIEW` remains a manual checkpoint
and that `BLOCK` remains an explicit stop state.
