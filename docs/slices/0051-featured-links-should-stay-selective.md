# Slice 0051 - Featured Links Should Stay Selective

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

Add an episode page that explains why featured links should stay selective.

## In Scope

- create one episode page about featured links
- link it to the concept and note pages that motivate curation

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain why not every page belongs in the featured set

## Main Business Rules

- featured links should stay high-signal
- the front door should not become a page dump
- the page should not become a navigation policy memo

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/021-featured-links-should-stay-selective.md` exists
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
- the page reinforces featured-link selectivity
- the change is represented in `work/changes/0014/implementation.md`

## Resolved Design Decisions

- keep the page short
- avoid turning it into a link taxonomy guide

