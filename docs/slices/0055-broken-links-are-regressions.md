# Slice 0055 - Broken Links Are Regressions

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

Add an episode page that says broken links are regressions, not minor annoyances.

## In Scope

- create one episode page about broken links
- link it to the concept and note pages that support link hygiene

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain why link integrity matters

## Main Business Rules

- broken links reduce trust
- link failures should be treated as maintenance issues
- the page should not become a QA checklist

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/022-broken-links-are-regressions.md` exists
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
- the page reinforces link integrity
- the change is represented in `work/changes/0015/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a tooling troubleshooting guide

