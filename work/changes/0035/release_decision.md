# Release Decision

- Change: `0035`
- Date: 2026-05-02
- Decision: accepted

## Decision Summary

The transcript-to-markdown draft slice is accepted as the intended internal
version for this request.

## Why

- transcript input is accepted directly
- idea extraction runs before reference enrichment
- markdown is the first durable output
- the flow is testable with fakes and validated by the full suite
- the model-backed path works in the current environment with `gemma3:1b`
- fallback behavior is deterministic when the model is slow or malformed

## Evidence

- `python3 -m pytest -q` passed with `109 passed`
- the real Portuguese transcript produced a markdown draft with `gemma3:1b`
- the CLI keeps working when the model path falls back

## Caveat

Reference enrichment still permits synthetic output for now. That is acceptable
for this release because the request was for markdown draft generation, not for
fully verified external reference curation.

## Notes

- site publishing remains out of scope
- raw video ingestion remains out of scope
- the accepted slice stays separate from the existing safety-and-release flow
