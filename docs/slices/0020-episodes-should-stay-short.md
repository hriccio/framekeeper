# Slice 0020 - Episodes Should Stay Short

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

Add an episode page that says episode pages should stay short and focused.

## In Scope

- create one episode page about episode length and shape
- link it back to the maintenance-related concept pages

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should keep episode pages focused on one idea

## Main Business Rules

- episodes should be short enough to scan
- one page should not try to cover the whole site
- the page should not become a style guide

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/008-episodes-should-stay-short.md` exists
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
- the page reinforces the short-form maintenance rule
- the change is represented in `work/changes/0008/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid expanding it into a design doctrine

