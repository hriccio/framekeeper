# Slice 0066 - Public Pages Are Refined

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

Add an episode page that says public pages should show refined content.

## In Scope

- create one episode page about public pages staying refined
- link it to the concept and note pages that support the boundary

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain why publication is an editing step

## Main Business Rules

- public pages should be shaped before they are exposed
- refinement improves clarity and usefulness
- the page should not become a process checklist

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/027-public-pages-are-refined.md` exists
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
- the page reinforces refined public content
- the change is represented in `work/changes/0017/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a publishing operations manual
