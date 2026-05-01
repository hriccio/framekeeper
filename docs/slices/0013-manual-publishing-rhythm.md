# Slice 0013 - Manual Publishing Rhythm

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

Add a concept page that favors continuity and manual editing over optimization
for the knowledge layer.

## In Scope

- create one concept page about publishing rhythm
- link it back to the episode and note pages that motivate it

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should describe a sustainable publishing rhythm

## Main Business Rules

- content should be easy to maintain over time
- manual editing comes before automation
- the page should not turn into a productivity manifesto

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/manual-publishing-rhythm.md` exists
- the home page links to the page
- the concepts index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the concepts index lists the page

## Scenario Definition

1. open the concept page
2. follow the links to the supporting pages

## Done Criteria

- the concept page exists and is linked
- the page preserves the manual-first publishing rhythm
- the change is represented in `work/changes/0006/implementation.md`

## Resolved Design Decisions

- keep the page short and practical
- avoid automation hype language

