# Slice 0129 - Release And Exposure Workflow

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

Add a note page that records the release and exposure workflow.

## In Scope

- create one note page about the path from release decision to exposure
- link it to the episode and concept pages that support the workflow

## Use-Case Contract

- input: manually authored note content
- output: one structured note page under `docs/notes/`
- behavior: the page should describe how accepted state becomes exposed

## Main Business Rules

- decide release explicitly
- prepare the accepted state in portable form
- expose the accepted state after release

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/notes/0026-release-and-exposure-workflow.md` exists
- the home page links to the page
- the notes index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the notes index lists the page

## Scenario Definition

1. open the note page
2. follow links to the related episode and concept pages

## Done Criteria

- the note page exists and is linked
- the page records the release and exposure workflow
- the change is represented in `work/changes/0029/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning the workflow into an operations manual
