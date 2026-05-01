# Slice 0035 - Older Pages Still Matter

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

Add an episode page that explains why older pages still matter in the site.

## In Scope

- create one episode page about older pages
- link it back to the versioning and archive-related concept pages

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain why older pages remain part of the site

## Main Business Rules

- old pages should not be abandoned silently
- updated thinking should remain visible over time
- the page should not become a changelog entry

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/014-older-pages-still-matter.md` exists
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
- the page reinforces archival accountability
- the change is represented in `work/changes/0011/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a history log

