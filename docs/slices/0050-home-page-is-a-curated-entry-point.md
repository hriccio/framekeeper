# Slice 0050 - Home Page Is A Curated Entry Point

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

Add an episode page that says the home page is a curated entry point, not a
full index dump.

## In Scope

- create one episode page about the home page
- link it back to the concept and note pages that support curation

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain the home page's role as a front door

## Main Business Rules

- the home page should be selective
- featured links should support discovery
- the page should not become a sitemap note

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/020-home-page-is-a-curated-entry-point.md` exists
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
- the page reinforces the home-page role
- the change is represented in `work/changes/0014/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a homepage redesign doc

