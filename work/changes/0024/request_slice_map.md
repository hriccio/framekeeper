# Request Slice Map

- Change: `0024`
- Request: `work/changes/0024/request.md`
- Status: accepted

## Request Boundary

Add five pages that keep exploratory video and durable page boundaries clear.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0100-videos-capture-thinking-in-motion.md` | accepted | Adds an episode page about videos capturing thinking in motion. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twenty.md` |
| `docs/slices/0101-refined-pages-preserve-the-idea.md` | accepted | Adds an episode page about refined pages preserving the idea. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twenty.md` |
| `docs/slices/0102-exploratory-videos-need-extraction.md` | accepted | Adds a concept page about exploratory videos needing extraction. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twenty.md` |
| `docs/slices/0103-durable-pages-outlast-the-recording.md` | accepted | Adds a concept page about durable pages outlasting the recording. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twenty.md` |
| `docs/slices/0104-thinking-in-motion-workflow.md` | accepted | Adds a note page describing the thinking-in-motion workflow. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twenty.md` |

## Out Of Scope

- automation and generation
- publishing infrastructure
- search and database support

## Open Questions

- none for this slice batch

## EGD Notes

Expectation-gap review should verify that the public site preserves the idea
from the video without pretending the recording itself is the final artifact.
