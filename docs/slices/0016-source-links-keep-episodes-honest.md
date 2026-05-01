# Slice 0016 - Source Links Keep Episodes Honest

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

Add an episode page that explains why source links matter for traceability and
editorial honesty.

## In Scope

- create one episode page about source links
- link it back to the relevant note and reference pages

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should preserve a visible path back to its source material

## Main Business Rules

- source links should remain explicit
- published content should not obscure its origin
- the episode page should not expose raw transcripts by default

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/007-source-links-keep-episodes-honest.md` exists
- the home page links to the page
- the episodes index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the episodes index lists the page

## Scenario Definition

1. open the episode page
2. follow the source link and supporting links

## Done Criteria

- the episode page exists and is linked
- the page keeps source provenance visible
- the change is represented in `work/changes/0007/implementation.md`

## Resolved Design Decisions

- keep the page focused on provenance, not on workflow mechanics
- avoid copying the source into the page body

