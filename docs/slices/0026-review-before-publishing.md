# Slice 0026 - Review Before Publishing

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

Add an episode page that says review comes before publishing.

## In Scope

- create one episode page about the review step
- link it to the concept and note pages that motivate the review cycle

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should make review a visible part of the content flow

## Main Business Rules

- review happens before publication
- review preserves human judgment
- the page should not become a publishing operations manual

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/011-review-before-publishing.md` exists
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
- the page preserves the review-before-publishing rule
- the change is represented in `work/changes/0009/implementation.md`

## Resolved Design Decisions

- keep the page focused on review
- avoid expanding it into an approval workflow manual

