# Slice 0146 - Transcript Markdown Draft Generation

## Status

Accepted.

## Selected Pack

- `python_ddd_monolith`

## Runtime Targets

- single Python runtime
- local deterministic execution for tests

## Architecture Mode

- DDD-inspired modular monolith
- thin application use case over deterministic domain components
- local model-backed extraction and enrichment adapters

## Intent

Turn an already-provided transcript into markdown draft content for the
knowledge layer by extracting ideas first and then enriching them with
references.

## In Scope

- accept transcript text directly as input
- extract one or more candidate ideas from the transcript
- enrich the extracted idea with reference suggestions or supporting links
- render the result as markdown draft content only
- keep the slice executable with fake model ports in tests

## Use-Case Contract

- input: transcript text and optional title or metadata
- output: one markdown draft artifact suitable for the knowledge layer
- behavior: idea extraction runs before reference enrichment
- behavior: the markdown draft should expose the extracted angle and supporting
  references
- behavior: the slice should not publish to GitHub Pages

## Main Business Rules

- transcript is already available, so raw-video ingestion is out of scope
- the draft should preserve the extracted editorial angle
- reference enrichment supports the draft but does not replace human editing
- markdown is the first durable output shape
- local model calls should be replaceable by fakes in tests

## Required Ports

- a model port for idea extraction
- a model or adapter port for reference enrichment
- a markdown draft renderer or writer port

## Out Of Scope

- raw video ingestion
- broader workflow orchestration outside Framekeeper
- GitHub Pages deployment
- automatic publication decisions
- safety classification changes

## Candidate Acceptance Criteria

- a transcript can be transformed into markdown draft content
- idea extraction happens before reference enrichment
- the markdown draft includes the extracted editorial angle
- the markdown draft includes reference enrichment output
- tests can exercise the flow without a live model dependency

## Initial Test Plan

- unit tests cover transcript-to-draft generation with fake model ports
- tests prove idea extraction feeds reference enrichment
- tests prove the markdown renderer receives the enriched structure

## Scenario Definition

1. submit a transcript with a clear editorial angle
2. extract the candidate idea from the transcript
3. enrich the idea with reference suggestions
4. render the markdown draft

## Done Criteria

- the transcript-to-markdown draft use case is implemented
- tests prove the flow is local and deterministic at the boundary
- the slice stays separate from the existing safety-and-release flow
