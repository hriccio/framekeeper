# Slice 0007 - Human Final Authority

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

Add a concept page that preserves the channel rule that Henrique remains the
final authority over meaning and publication.

## In Scope

- create one concept page about human final authority
- link it back to the relevant episode pages

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the concept should define the boundary rather than narrate the whole system

## Main Business Rules

- automation may assist
- meaning and publication remain human decisions
- the concept page should stay reusable across multiple episodes

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/human-final-authority.md` exists
- the home page links to the page
- the concepts index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the concepts index lists the page

## Scenario Definition

1. open the concept page
2. follow links to the episode pages that use it

## Done Criteria

- the concept page exists and is linked
- the page captures the authority boundary without drifting into process detail
- the change is represented in `work/changes/0005/implementation.md`

## Resolved Design Decisions

- write the page as a reusable concept, not an episode recap
- keep the wording concise and durable

