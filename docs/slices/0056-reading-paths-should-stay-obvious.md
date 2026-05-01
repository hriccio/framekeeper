# Slice 0056 - Reading Paths Should Stay Obvious

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

Add an episode page that says reading paths should stay obvious.

## In Scope

- create one episode page about reading paths
- link it to the concept and note pages that motivate the path

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain why the reader path matters

## Main Business Rules

- reading paths should be easy to follow
- link structure should support the expected journey
- the page should not become a navigation diagram

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/023-reading-paths-should-stay-obvious.md` exists
- the home page links to the page
- the episodes index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the episodes index lists the page

## Scenario Definition

1. open the episode page
2. follow the links to the supporting concept and note pages

## Done Criteria

- the episode page exists and is linked
- the page reinforces obvious reading paths
- the change is represented in `work/changes/0015/implementation.md`

## Resolved Design Decisions

- keep the page short
- avoid turning it into a site architecture spec

