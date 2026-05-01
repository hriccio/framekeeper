# Slice 0080 - Sources Need Refresh Cycles

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

Add an episode page about refreshing sources to keep them useful.

## In Scope

- create one episode page about sources needing refresh cycles
- link it to the concept and note pages that support source currency

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain why external sources need review

## Main Business Rules

- sources age
- time-sensitive evidence should be rechecked
- the page should not become a general citation lesson

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/032-sources-need-refresh-cycles.md` exists
- the home page links to the page
- the episodes index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the episodes index lists the page

## Scenario Definition

1. open the episode page
2. follow links to the supporting concept and note pages

## Done Criteria

- the episode page exists and is linked
- the page reinforces source refresh cycles
- the change is represented in `work/changes/0020/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a link-checking manual
