# Slice 0103 - Durable Pages Outlast The Recording

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

Add a concept page about durable pages outlasting the recording.

## In Scope

- create one concept page about durability across the recording boundary

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should explain why pages must stand alone

## Main Business Rules

- durable pages should outlast the recording
- the page should remain understandable on its own
- the page should stay short and reusable

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/durable-pages-outlast-the-recording.md` exists
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
- the page reinforces durability after recording
- the change is represented in `work/changes/0024/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into an archival note
