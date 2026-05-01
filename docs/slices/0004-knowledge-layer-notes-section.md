# Slice 0004 - Knowledge Layer Notes Section

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

Add the notes section from the knowledge-layer content model:

- a `docs/notes/` index
- one seeded note page
- links from the home page and the notes index

## In Scope

- create a notes index
- create one note page
- link the home page to the notes section
- link the notes index to the seeded note page

## Use-Case Contract

- input: manually authored note content
- output: browsable notes pages under `docs/notes/`
- behavior: the notes section remains separate from raw transcripts and from the refined episode pages

## Main Business Rules

- notes are intermediate or semi-refined artifacts
- raw transcripts remain outside the published tree
- notes are not a substitute for episode pages or concept pages

## Required Ports

- none

## Out Of Scope

- transcript automation
- content generation automation
- publishing automation
- database support
- search support

## Candidate Acceptance Criteria

- `docs/notes/index.md` exists
- `docs/notes/0001-working-notes.md` exists
- the home page links to the notes section
- the notes index lists the seeded note

## Initial Test Plan

- a test verifies the notes files exist
- a test verifies the home page links to the notes section
- a test verifies the notes index links to the seeded note

## Scenario Definition

1. open the home page
2. open the notes section
3. open the seeded note page

## Done Criteria

- the notes section exists and is navigable
- the notes artifact type is distinct from episodes, concepts, and references
- tests confirm the new section and navigation
- the change is represented in `work/changes/0004/implementation.md`

## Resolved Design Decisions

- keep notes short and manually authored
- use notes as a distinct, non-raw intermediate artifact type
- seed the section with one note page about the content model

