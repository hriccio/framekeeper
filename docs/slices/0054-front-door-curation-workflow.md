# Slice 0054 - Front Door Curation Workflow

## Status

Accepted.

## Selected Pack

- documentation-first, no runtime pack change

## Runtime Targets

- GitHub Pages from `docs/`
- local markdown browsing and link checking

## Architecture Mode

- static markdown content layer
- manual authorship first

## Intent

Add a note page that records how the home page and featured links are curated.

## In Scope

- create one note page about front-door curation
- link it to the episode and concept pages that support the workflow

## Use-Case Contract

- input: manually authored note content
- output: one structured note page under `docs/notes/`
- behavior: the note should explain how the front door stays selective

## Main Business Rules

- the front door should stay high-signal
- featured links should be maintained intentionally
- the note should not turn into a homepage maintenance checklist

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/notes/0011-front-door-curation-workflow.md` exists
- the home page links to the page
- the notes index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the notes index lists the page

## Scenario Definition

1. open the note page
2. follow the links to the pages it references

## Done Criteria

- the note page exists and is linked
- the page preserves the front-door curation boundary
- the change is represented in `work/changes/0014/implementation.md`

## Resolved Design Decisions

- keep the note concise
- avoid turning it into a complete site governance manual

