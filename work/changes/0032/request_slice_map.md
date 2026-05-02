# Request Slice Map

- Change: `0032`
- Request: `work/changes/0032/request.md`
- Status: accepted

## Request Boundary

Add five pages that explain how editorial angle and evidence weight help classify
transcript-derived ideas into the right public page shape.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0140-transcript-fragments-need-an-editorial-angle.md` | accepted | Adds an episode page about transcript fragments needing an editorial angle. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentyeight.py` |
| `docs/slices/0141-source-rich-ideas-belong-in-references.md` | accepted | Adds an episode page about source-rich ideas belonging in references. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentyeight.py` |
| `docs/slices/0142-editorial-angle-guides-family-choice.md` | accepted | Adds a concept page about editorial angle guiding page family choice. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentyeight.py` |
| `docs/slices/0143-evidence-weight-shapes-content-form.md` | accepted | Adds a concept page about evidence weight shaping content form. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentyeight.py` |
| `docs/slices/0144-transcript-classification-checklist.md` | accepted | Adds a note page describing the transcript classification checklist. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentyeight.py` |

## Out Of Scope

- automation and generation
- publishing infrastructure
- search and database support

## Open Questions

- none for this slice batch

## EGD Notes

Expectation-gap review should verify that the pages stay on the content side:
they should help classify transcript-derived ideas, not describe repository
workflow.
