# Slice 0070 - Ideas Are Extracted From Videos

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

Add an episode page that says ideas are extracted from videos for the knowledge
layer.

## In Scope

- create one episode page about extracting ideas from videos
- link it to the concept and note pages that support extraction

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain how ideas move into the knowledge layer

## Main Business Rules

- extraction is selective
- the video is source material, not the final artifact
- the page should not become an editing manual

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/028-ideas-are-extracted-from-videos.md` exists
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
- the page reinforces idea extraction
- the change is represented in `work/changes/0018/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a transcript-processing tutorial
