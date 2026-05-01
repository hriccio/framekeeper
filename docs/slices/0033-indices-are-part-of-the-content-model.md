# Slice 0033 - Indices Are Part Of The Content Model

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

Add a concept page that treats indices as part of the content model, not just
navigation utilities.

## In Scope

- create one concept page about indices
- link it to the episodes and note pages that motivate the idea

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should explain why indices deserve explicit maintenance

## Main Business Rules

- indices should stay accurate
- indices should be updated with the pages they represent
- the page should not become a site-map manifesto

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/indices-are-part-of-the-content-model.md` exists
- the home page links to the page
- the concepts index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the concepts index lists the page

## Scenario Definition

1. open the concept page
2. follow the links to the episode and note pages it references

## Done Criteria

- the concept page exists and is linked
- the page preserves the index discipline
- the change is represented in `work/changes/0010/implementation.md`

## Resolved Design Decisions

- keep the page concise and operational
- avoid duplicating the maintenance workflow note

