# Slice 0125 - Release Decisions Stay Explicit

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

Add an episode page about keeping release decisions explicit.

## In Scope

- create one episode page about the release decision boundary
- link it to the concept and note pages that support release and exposure

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain why release must be recorded explicitly

## Main Business Rules

- release is a conscious human judgment
- acceptance should be visible
- exposure is separate from the decision to release

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/050-release-decisions-stay-explicit.md` exists
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
- the page reinforces explicit release decisions
- the change is represented in `work/changes/0029/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid making release look automatic
