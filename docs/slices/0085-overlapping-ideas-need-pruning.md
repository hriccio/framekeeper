# Slice 0085 - Overlapping Ideas Need Pruning

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

Add an episode page about overlapping ideas needing pruning.

## In Scope

- create one episode page about pruning overlap
- link it to the concept and note pages that support pruning

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain why redundant overlap is a maintenance issue

## Main Business Rules

- overlapping ideas should be reduced
- the clearest version should remain
- the page should not become a repetition of other pages

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/034-overlapping-ideas-need-pruning.md` exists
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
- the page reinforces pruning overlap
- the change is represented in `work/changes/0021/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a general editing manual
