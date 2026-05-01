# Slice 0038 - Archival Pages Stay Linked

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

Add a concept page that keeps archival pages linked from the active site.

## In Scope

- create one concept page about archival linking
- link it to the episode and note pages that motivate it

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should describe why archived pages should remain reachable

## Main Business Rules

- archival pages should remain reachable from the site
- links should preserve context across updates
- the page should not become a sitemap specification

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/archival-pages-stay-linked.md` exists
- the home page links to the page
- the concepts index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the concepts index lists the page

## Scenario Definition

1. open the concept page
2. follow links to the episode and note pages it references

## Done Criteria

- the concept page exists and is linked
- the page preserves archival linkability
- the change is represented in `work/changes/0011/implementation.md`

## Resolved Design Decisions

- keep the page short and operational
- avoid turning it into a navigation policy manual

