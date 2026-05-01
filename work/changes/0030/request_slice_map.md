# Request Slice Map

- Change: `0030`
- Request: `work/changes/0030/request.md`
- Status: accepted

## Request Boundary

Add five pages that make post-exposure feedback explicit in the public
knowledge layer.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0130-feedback-follows-exposure.md` | accepted | Adds an episode page about feedback following exposure. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentysix.py` |
| `docs/slices/0131-feedback-feeds-the-next-request.md` | accepted | Adds an episode page about feedback feeding the next request. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentysix.py` |
| `docs/slices/0132-feedback-is-distinct-from-signal.md` | accepted | Adds a concept page about feedback being distinct from signal. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentysix.py` |
| `docs/slices/0133-feedback-reopens-the-loop.md` | accepted | Adds a concept page about feedback reopening the loop. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentysix.py` |
| `docs/slices/0134-feedback-capture-workflow.md` | accepted | Adds a note page describing the feedback capture workflow. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentysix.py` |

## Out Of Scope

- automation and generation
- publishing infrastructure
- search and database support

## Open Questions

- none for this slice batch

## EGD Notes

Expectation-gap review should verify that feedback is described as post-
exposure evidence for the next loop, not as internal signal scoring.
