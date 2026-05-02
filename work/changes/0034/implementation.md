# Implementation

Implemented a CLI for transcript-idea family classification.

## Added Code

- `src/app/interfaces/cli/classify_transcript_idea.py`

## Added Tests

- `tests/integration/test_classify_transcript_idea_cli.py`

## Behavior

- accepts a transcript, optional title, and video ID
- prints a readable family recommendation summary
- reuses the deterministic transcript-idea classifier

## Validation

- CLI test covers the classification output
