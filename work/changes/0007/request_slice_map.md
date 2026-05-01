# Request Slice Map

- Change: `0007`
- Request: `work/changes/0007/request.md`
- Status: accepted

## Request Boundary

Add five pages that clarify how references and source material support the
knowledge layer.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0015-references-support-episodes.md` | accepted | Adds an episode page about references supporting episodes. | `tests/integration/test_knowledge_layer_next_five_pages_batch_three.py` |
| `docs/slices/0016-source-links-keep-episodes-honest.md` | accepted | Adds an episode page about source links preserving honesty and traceability. | `tests/integration/test_knowledge_layer_next_five_pages_batch_three.py` |
| `docs/slices/0017-curated-references-are-evidence.md` | accepted | Adds a concept page that frames curated references as evidence, not filler. | `tests/integration/test_knowledge_layer_next_five_pages_batch_three.py` |
| `docs/slices/0018-youtube-community-guidelines-reference.md` | accepted | Adds a reference page for the YouTube policy source used by the project. | `tests/integration/test_knowledge_layer_next_five_pages_batch_three.py` |
| `docs/slices/0019-reference-curation-workflow.md` | accepted | Adds a note page that records the reference curation workflow. | `tests/integration/test_knowledge_layer_next_five_pages_batch_three.py` |

## Out Of Scope

- automation and generation
- publishing infrastructure
- search and database support

## Open Questions

- none for this slice batch

## EGD Notes

Expectation-gap review should verify that source and reference pages support the
content layer without replacing it, and that links remain local and coherent.

