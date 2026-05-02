# Slice 0140 - Transcript Fragments Need An Editorial Angle

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

Add an episode page about transcript fragments needing an editorial angle.

## In Scope

- create one episode page about editorial angle as a classification cue
- link it to the concept and note pages that support page-family choice

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain why angle comes before drafting

## Main Business Rules

- the angle should be visible early
- page shape follows the angle
- not every fragment wants the same family

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/056-transcript-fragments-need-an-editorial-angle.md` exists
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
- the page reinforces editorial angle as a classification cue
- the change is represented in `work/changes/0032/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a general editing manual
