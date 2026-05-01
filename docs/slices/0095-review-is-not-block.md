# Slice 0095 - Review Is Not Block

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

Add an episode page about review not being block.

## In Scope

- create one episode page about the review state
- link it to the concept and note pages that support the safety tier model

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain why review is a checkpoint, not a stop

## Main Business Rules

- review is for human judgment
- review should not end the workflow
- the page should not become a policy glossary entry

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/038-review-is-not-block.md` exists
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
- the page reinforces review as a checkpoint
- the change is represented in `work/changes/0023/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a risk glossary
