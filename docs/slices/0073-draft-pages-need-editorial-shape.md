# Slice 0073 - Draft Pages Need Editorial Shape

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

Add a concept page about draft pages needing editorial shape.

## In Scope

- create one concept page about draft pages needing editorial shape

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should explain why drafts are already shaped artifacts

## Main Business Rules

- drafts should show their intended direction
- the shape should stay visible across revisions
- the page should stay focused on editorial structure

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/draft-pages-need-editorial-shape.md` exists
- the home page links to the page
- the concepts index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the concepts index lists the page

## Scenario Definition

1. open the concept page
2. follow links to the related episode pages

## Done Criteria

- the concept page exists and is linked
- the page reinforces editorial shape in drafts
- the change is represented in `work/changes/0018/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid making it a design system note
