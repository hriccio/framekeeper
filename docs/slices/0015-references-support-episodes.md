# Slice 0015 - References Support Episodes

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

Add an episode page that says references support the episodes instead of
substituting for them.

## In Scope

- create one episode page about the role of references
- link it back to the concept and reference pages it depends on

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should present references as support material

## Main Business Rules

- episodes remain the primary storytelling layer
- references provide support and traceability
- the episode page should not become a bibliography dump

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/006-references-support-episodes.md` exists
- the home page links to the page
- the episodes index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the episodes index lists the page

## Scenario Definition

1. open the episode page
2. follow links to the related concept and reference page

## Done Criteria

- the episode page exists and is linked
- the page frames references as support material
- the change is represented in `work/changes/0007/implementation.md`

## Resolved Design Decisions

- keep the page short and explanatory
- avoid using the page as a general research essay

