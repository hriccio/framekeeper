# Slice 0099 - Safety Tier Workflow

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

Add a note page that records the safety tier workflow.

## In Scope

- create one note page about moving through review, block, and override

## Use-Case Contract

- input: manually authored note content
- output: one structured note page under `docs/notes/`
- behavior: the page should describe how the safety tiers are used

## Main Business Rules

- use review for human attention
- use block for hard stops
- keep overrides explicit

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/notes/0020-safety-tier-workflow.md` exists
- the home page links to the page
- the notes index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the notes index lists the page

## Scenario Definition

1. open the note page
2. follow links to the related concept and episode pages

## Done Criteria

- the note page exists and is linked
- the page reinforces the safety tier workflow
- the change is represented in `work/changes/0023/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into an enforcement manual
