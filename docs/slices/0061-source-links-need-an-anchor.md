# Slice 0061 - Source Links Need An Anchor

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

Add an episode page that says source links need an anchor in the claim they
support.

## In Scope

- create one episode page about source link anchoring
- link it to the concept and note pages that support reference discipline

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain why source links need context

## Main Business Rules

- source links need a visible reason to exist
- the claim should make the link readable
- the page should not become a navigation tutorial

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/025-source-links-need-an-anchor.md` exists
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
- the page reinforces source link discipline
- the change is represented in `work/changes/0016/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a source citation primer
