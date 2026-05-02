# Implementation

Implemented a transcript-to-family classifier for the knowledge layer.

## Added Code

- `src/app/domain/content_classification.py`
- `src/app/application/classify_transcript_idea.py`

## Added Tests

- `tests/unit/test_classify_transcript_idea.py`

## Added Slice Doc

- `docs/slices/0145-transcript-idea-family-classification.md`

## Behavior

- source-heavy ideas map to `REFERENCE`
- workflow/checklist ideas map to `NOTE`
- explanatory or principle-driven ideas map to `CONCEPT`
- generic narrative ideas default to `EPISODE`

## Validation

- unit tests cover the deterministic family classifier
