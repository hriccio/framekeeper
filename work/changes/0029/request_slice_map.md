# Request Slice Map

- Change: `0029`
- Request: `work/changes/0029/request.md`
- Status: accepted

## Request Boundary

Add five pages that make release and exposure explicit in the public knowledge
layer.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0125-release-decisions-stay-explicit.md` | accepted | Adds an episode page about keeping release decisions explicit. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentyfive.py` |
| `docs/slices/0126-exposure-follows-acceptance.md` | accepted | Adds an episode page about exposure following acceptance. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentyfive.py` |
| `docs/slices/0127-release-is-not-exposure.md` | accepted | Adds a concept page about release not being the same as exposure. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentyfive.py` |
| `docs/slices/0128-portable-artifacts-support-exposure.md` | accepted | Adds a concept page about portable artifacts supporting exposure. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentyfive.py` |
| `docs/slices/0129-release-and-exposure-workflow.md` | accepted | Adds a note page describing the release and exposure workflow. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentyfive.py` |

## Out Of Scope

- automation and generation
- publishing infrastructure
- search and database support

## Open Questions

- none for this slice batch

## EGD Notes

Expectation-gap review should verify that release remains a human decision and
that exposure is described as a separate operational step.
