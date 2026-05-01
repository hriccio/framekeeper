# Slice 0121 - Lightweight EGD Is The Earlier-Stage Default

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

Add an episode page explaining that lightweight EGD is the earlier-stage
default when deterministic scenario evidence is not yet available.

## In Scope

- create one episode page about lightweight expectation-gap detection
- link it to the concept and note pages that support evaluation review

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain when artifact-led review is appropriate

## Main Business Rules

- use lightweight EGD when no scenario packet exists
- review semantic artifacts and fresh test evidence directly
- do not pretend a fuller scenario run happened

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/049-lightweight-egd-is-the-earlier-stage-default.md` exists
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
- the page reinforces lightweight review as the earlier-stage default
- the change is represented in `work/changes/0028/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid presenting lightweight review as a fallback failure
