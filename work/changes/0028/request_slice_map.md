# Request Slice Map

- Change: `0028`
- Request: `work/changes/0028/request.md`
- Status: accepted

## Request Boundary

Add five pages that make scenario evaluation and validation modes explicit in
the public knowledge layer.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0120-scenario-evaluation-is-not-tests.md` | accepted | Adds an episode page explaining that scenario evaluation complements tests rather than replacing them. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentyfour.py` |
| `docs/slices/0121-lightweight-egd-is-the-earlier-stage-default.md` | accepted | Adds an episode page explaining that lightweight EGD is the earlier-stage default when deterministic scenario evidence is absent. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentyfour.py` |
| `docs/slices/0122-validation-modes-guide-slice-strategy.md` | accepted | Adds a concept page explaining how validation modes guide slice strategy. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentyfour.py` |
| `docs/slices/0123-deterministic-packets-keep-evidence-reviewable.md` | accepted | Adds a concept page explaining why compact deterministic packets keep evidence reviewable. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentyfour.py` |
| `docs/slices/0124-scenario-evaluation-workflow.md` | accepted | Adds a note page that records the practical scenario evaluation workflow. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentyfour.py` |

## Out Of Scope

- automation and generation
- publishing infrastructure
- search and database support

## Open Questions

- none for this slice batch

## EGD Notes

Expectation-gap review should verify that scenario evaluation is described as a
review loop, not as a substitute for tests or deterministic validation.
