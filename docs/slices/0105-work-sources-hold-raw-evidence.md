# Slice 0105 - Work Sources Hold Raw Evidence

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

Add an episode page about `work/sources` holding raw evidence.

## In Scope

- create one episode page about raw evidence storage
- link it to the concept and note pages that support repository memory

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain why raw evidence stays in `work/sources`

## Main Business Rules

- raw evidence belongs in `work/sources`
- the published site should not become the source store
- the page should not become a filesystem guide

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/042-work-sources-hold-raw-evidence.md` exists
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
- the page reinforces `work/sources` as raw evidence storage
- the change is represented in `work/changes/0025/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a repository-structure manual
