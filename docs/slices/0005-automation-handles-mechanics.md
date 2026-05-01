# Slice 0005 - Automation Handles Mechanics

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

Add an episode page that states the core boundary clearly:

> automation handles mechanics; Henrique handles meaning

## In Scope

- create one episode page about the mechanical role of automation
- link the page to the relevant concept pages
- keep the page small and human-readable

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should emphasize that automation does not own meaning

## Main Business Rules

- automation assists with mechanical processing
- human judgment owns meaning and publication
- the episode page should not become a transcript dump

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/002-automation-handles-mechanics.md` exists
- the home page links to the page
- the episodes index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the episodes index lists the page

## Scenario Definition

1. open the home page
2. open the episode page
3. follow the related concept links

## Done Criteria

- the episode page exists and is linked
- the page reinforces the mechanics-versus-meaning boundary
- the change is represented in `work/changes/0005/implementation.md`

## Resolved Design Decisions

- use a short episode page rather than a long essay
- link to existing concepts rather than duplicating them

