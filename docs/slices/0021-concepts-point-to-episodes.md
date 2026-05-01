# Slice 0021 - Concepts Point To Episodes

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

Add an episode page that shows concept pages should point back to the episodes
that motivate them.

## In Scope

- create one episode page about concept-page linking
- link it to the related concept pages

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should describe why concepts need episode context

## Main Business Rules

- concepts should be reusable across episodes
- concept pages need visible episode links
- the page should not become a link-policy memo

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/009-concepts-point-to-episodes.md` exists
- the home page links to the page
- the episodes index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the episodes index lists the page

## Scenario Definition

1. open the episode page
2. follow the links to the concept pages it references

## Done Criteria

- the episode page exists and is linked
- the page reinforces the concept-to-episode relationship
- the change is represented in `work/changes/0008/implementation.md`

## Resolved Design Decisions

- keep the page short and practical
- avoid broadening it into a content model spec

