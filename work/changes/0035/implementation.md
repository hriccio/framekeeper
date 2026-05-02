# Implementation

Implemented the transcript-to-markdown draft slice for the knowledge layer.

## Added Code

- `src/app/domain/markdown_draft.py`
- `src/app/application/ports/markdown_draft_generation.py`
- `src/app/application/generate_markdown_draft.py`
- `src/app/infrastructure/ollama/markdown_draft_generation.py`
- `src/app/interfaces/cli/generate_markdown_draft.py`

## Added Tests

- `tests/unit/test_generate_markdown_draft.py`
- `tests/integration/test_generate_markdown_draft_cli.py`

## Behavior

- accepts transcript text directly with optional title and metadata
- extracts one candidate idea before enriching references
- renders a markdown draft that preserves the editorial angle and source metadata
- uses Ollama-backed adapters by default while keeping the application layer on ports
- strips SRT noise and caps each Ollama prompt to a short transcript summary
- defaults each Ollama call to a 60-second timeout before falling back
- falls back to a deterministic local draft when Ollama times out or returns invalid output
- stays deterministic in tests by injecting fakes

## Validation

- `python3 -m pytest -q`
- result: `109 passed`
