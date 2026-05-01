# Slice 0065 - Raw Transcripts Stay Private

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

Add an episode page that says raw transcripts stay private by default.

## In Scope

- create one episode page about transcript privacy
- link it to the concept and note pages that support the boundary

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain why transcripts stay in the working layer

## Main Business Rules

- raw transcripts are not public content by default
- public exposure requires deliberate selection
- the page should not become a storage-policy manual

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/026-raw-transcripts-stay-private.md` exists
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
- the page reinforces transcript privacy
- the change is represented in `work/changes/0017/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a retention policy document
