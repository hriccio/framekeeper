# Slice 0009 - Raw And Refined Routing

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

Add a note page that explains how raw evidence becomes refined knowledge-layer
content without collapsing the two together.

## In Scope

- create one note page about raw versus refined routing
- link it to the episode and concept pages

## Use-Case Contract

- input: manually authored note content
- output: one structured note page under `docs/notes/`
- behavior: the note should describe the routing between raw inputs and refined pages

## Main Business Rules

- raw evidence stays outside the published site
- refined pages are the published knowledge layer
- notes may describe the workflow, but they are not raw evidence

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/notes/0002-raw-and-refined-routing.md` exists
- the home page links to the page
- the notes index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the notes index links to the page

## Scenario Definition

1. open the note page
2. follow links to the episode and concept pages it references

## Done Criteria

- the note page exists and is linked
- the page preserves the raw-versus-refined boundary
- the change is represented in `work/changes/0005/implementation.md`

## Resolved Design Decisions

- keep the note short and explanatory
- avoid using the note as a place for raw transcript capture

