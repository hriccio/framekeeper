# Slice 0046 - Summaries Preserve Gist

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

Add an episode page that explains how summaries preserve gist without replacing
the page.

## In Scope

- create one episode page about summaries
- link it to the concept and note pages that motivate the summary rule

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain why summaries stay secondary

## Main Business Rules

- summaries should help readers scan
- summaries should not replace the page itself
- the page should not become a summary-writing tutorial

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/019-summaries-preserve-gist.md` exists
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
- the page reinforces summary discipline
- the change is represented in `work/changes/0013/implementation.md`

## Resolved Design Decisions

- keep the page focused on gist
- avoid turning it into a generic writing aid

