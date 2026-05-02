# Request

- Change: `0033`
- Date: 2026-05-01

## Request Boundary

Implement a deterministic transcript-idea classifier that recommends the
public knowledge-layer family an extracted idea should become.

The classifier should help route transcript-derived ideas into:

- episodes
- concepts
- references
- notes

## Success Expectations

- source-heavy ideas map to `REFERENCE`
- workflow or checklist ideas map to `NOTE`
- explanatory or principle-driven ideas map to `CONCEPT`
- generic narrative ideas default to `EPISODE`
- the classifier stays independent from safety scoring
- the classifier returns a readable rationale for the recommendation

## Out Of Scope

- automatic publishing
- knowledge-layer page generation
- workflow tracing artifacts
- transcript transcription itself
- safety classification changes
