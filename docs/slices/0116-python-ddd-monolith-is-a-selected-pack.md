# Slice 0116 - Python DDD Monolith Is A Selected Pack

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

Add an episode page about the Python DDD monolith being a selected pack.

## In Scope

- create one episode page about the current pack choice
- link it to the concept and note pages that support pack selection

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain why the current pack is explicit and local

## Main Business Rules

- the selected pack should be visible
- the pack is a default, not the definition of MRL
- the page should not become a language debate

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/047-python-ddd-monolith-is-a-selected-pack.md` exists
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
- the page reinforces the current pack choice
- the change is represented in `work/changes/0027/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a platform preference note
