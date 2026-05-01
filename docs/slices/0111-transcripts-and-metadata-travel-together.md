# Slice 0111 - Transcripts And Metadata Travel Together

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

Add an episode page about transcripts and metadata traveling together.

## In Scope

- create one episode page about transcript and metadata pairing
- link it to the concept and note pages that support processing visibility

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain why the transcript needs its context

## Main Business Rules

- transcripts need context
- metadata supports interpretation
- the page should not become a data schema note

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/045-transcripts-and-metadata-travel-together.md` exists
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
- the page reinforces transcript/metadata pairing
- the change is represented in `work/changes/0026/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a metadata primer
