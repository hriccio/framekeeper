# Slice 0012 - WNT And CodingZen Stay Separate

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

Add a concept page that keeps the knowledge layer distinct from WastingNoTime
and CodingZen.

## In Scope

- create one concept page about site separation
- link it back to the relevant episode and note pages

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should explain why this site stays separate

## Main Business Rules

- this knowledge layer is its own site
- WastingNoTime remains more curated and structurally clean
- CodingZen remains focused on exploration, creative coding, and play

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/wnt-and-codingzen-stay-separate.md` exists
- the home page links to the page
- the concepts index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the concepts index lists the page

## Scenario Definition

1. open the concept page
2. follow links back to the episode and note pages that motivate it

## Done Criteria

- the concept page exists and is linked
- the page preserves the repository-family boundary
- the change is represented in `work/changes/0006/implementation.md`

## Resolved Design Decisions

- write the separation as an explicit concept, not a throwaway note
- keep the wording clear enough to survive future repository growth

