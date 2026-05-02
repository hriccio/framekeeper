# Request

- Change: `0035`
- Date: 2026-05-01

## Request Boundary

Define a bounded runtime slice for turning an already-provided transcript into
a markdown draft for the knowledge layer by using local Llama-backed idea
extraction and reference enrichment.

## Success Expectations

- transcript input is accepted directly, without raw video ingestion
- idea extraction happens before reference enrichment
- the output is markdown only at first
- the flow stays local and testable with fake model ports
- the slice does not include site publishing

## Out Of Scope

- raw video ingestion
- orchestration of the broader external flow
- GitHub Pages deployment
- automatic publication decisions
