# Request Slice Map

- Change: `0003`
- Request: `work/changes/0003/request.md`
- Status: accepted

## Request Boundary

Add a small but real knowledge-layer content seed so the GitHub Pages site has
an actual example episode, concept, and reference page.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0003-knowledge-layer-content-seed.md` | accepted | Covers the full request by adding one content page in each major section and linking them from the site shell. | `tests/integration/test_knowledge_layer_content_seed.py`, `docs/index.md`, `docs/episodes/index.md`, `docs/concepts/index.md`, `docs/references/index.md` |

## Out Of Scope

- automation and generation
- publishing infrastructure
- search and database support

## Open Questions

- none for this slice

## EGD Notes

Expectation-gap review should verify that the site now has representative
content, that the links are local and consistent, and that the example pages do
not reintroduce raw transcript behavior.

