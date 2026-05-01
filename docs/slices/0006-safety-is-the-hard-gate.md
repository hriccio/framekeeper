# Slice 0006 - Safety Is The Hard Gate

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

Add an episode page that records the safety boundary as the only blocking
stage in the workflow.

## In Scope

- create one episode page about the safety gate
- connect it to the safety/signal concept page
- keep the page distinct from signal feedback content

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should say that safety is the only blocking stage

## Main Business Rules

- safety can block
- signal cannot block
- the page should not confuse policy risk with quality judgment

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/003-safety-is-the-hard-gate.md` exists
- the home page links to the page
- the episodes index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the episodes index lists the page

## Scenario Definition

1. open the home page
2. open the safety episode page
3. follow the safety/signal concept link

## Done Criteria

- the episode page exists and is linked
- the page reinforces the blocking boundary
- the change is represented in `work/changes/0005/implementation.md`

## Resolved Design Decisions

- keep the page focused on the hard gate only
- avoid mixing safety with signal diagnostics

