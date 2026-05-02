# Impact Analysis

## Scope

This change introduces a new runtime boundary for transcript-to-markdown draft
generation. It affects the knowledge-layer side of Framekeeper but not the
existing raw-video processing flow.

## Affected Areas

- `src/app/application/`
- `src/app/domain/`
- `src/app/interfaces/`
- `tests/unit/`
- `tests/integration/`
- `docs/slices/0146-transcript-markdown-draft-generation.md`
- `docs/semantics/model_hypothesis.md`
- `docs/semantics/domain_background_knowledge.md`

## Tension To Watch

The new flow should stay model-backed but not model-dependent at runtime
testing time. The implementation needs a fake or stub path so the markdown
draft can be exercised deterministically.

The slice should generate markdown only. Site publishing is a later concern.

## Regression Risk

Medium. The flow crosses extraction, reference enrichment, and rendering, so
the main risk is collapsing those concerns into one opaque step or letting the
model output leak directly into public-facing content without a stable shape.
