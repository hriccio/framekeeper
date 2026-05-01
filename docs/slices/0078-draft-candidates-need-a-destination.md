# Slice 0078 - Draft Candidates Need A Destination

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

Add a concept page about draft candidates needing a destination.

## In Scope

- create one concept page about draft candidates needing a destination

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should explain why candidates should not stay directionless

## Main Business Rules

- candidate ideas should move toward a family
- direction makes the draft easier to edit
- the page should stay focused on destination, not process

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/draft-candidates-need-a-destination.md` exists
- the home page links to the page
- the concepts index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the concepts index lists the page

## Scenario Definition

1. open the concept page
2. follow links to the related episode pages

## Done Criteria

- the concept page exists and is linked
- the page reinforces candidate direction
- the change is represented in `work/changes/0019/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a workflow diagram
