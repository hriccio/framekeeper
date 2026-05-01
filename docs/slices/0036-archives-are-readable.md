# Slice 0036 - Archives Are Readable

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

Add an episode page that says archives should remain readable after changes.

## In Scope

- create one episode page about archive readability
- link it to the versioning-related concept and note pages

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should describe how archived material remains useful

## Main Business Rules

- archived pages should stay understandable
- archives should preserve the ability to trace prior thinking
- the page should not become a maintenance policy memo

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/015-archives-are-readable.md` exists
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
- the page reinforces archive readability
- the change is represented in `work/changes/0011/implementation.md`

## Resolved Design Decisions

- keep the page focused on readability, not preservation mechanics
- avoid broadening it into repository history guidance

