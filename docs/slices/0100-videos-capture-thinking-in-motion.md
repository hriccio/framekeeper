# Slice 0100 - Videos Capture Thinking In Motion

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

Add an episode page about videos capturing thinking in motion.

## In Scope

- create one episode page about the live recording state
- link it to the concept and note pages that support extraction

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain why the recording remains valuable source material

## Main Business Rules

- videos capture the idea in motion
- the recording is useful before refinement
- the page should not become a transcript defense

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/040-videos-capture-thinking-in-motion.md` exists
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
- the page reinforces recording as source material
- the change is represented in `work/changes/0024/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a media archive note
