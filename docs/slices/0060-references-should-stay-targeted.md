# Slice 0060 - References Should Stay Targeted

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

Add an episode page that says references should stay targeted to the idea they
support.

## In Scope

- create one episode page about targeted references
- link it to the concept and note pages that support reference discipline

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain why references should stay selective

## Main Business Rules

- references should support the claim, not widen the topic
- the list should stay curated
- the page should not become a link dump

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/024-references-should-stay-targeted.md` exists
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
- the page reinforces targeted reference use
- the change is represented in `work/changes/0016/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a bibliography guide
