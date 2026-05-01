# Slice 0135 - Requests Need Clear Boundaries

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

Add an episode page about requests needing clear boundaries.

## In Scope

- create one episode page about the request boundary
- link it to the concept and note pages that support request-to-slice mapping

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain why requests need a clear boundary

## Main Business Rules

- request boundaries must stay explicit
- implementation should not redefine the request
- review depends on a bounded intent

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/054-requests-need-clear-boundaries.md` exists
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
- the page reinforces request boundaries
- the change is represented in `work/changes/0031/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid collapsing request and implementation
