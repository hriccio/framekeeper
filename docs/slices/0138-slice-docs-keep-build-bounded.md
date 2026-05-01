# Slice 0138 - Slice Docs Keep Build Bounded

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

Add a concept page about slice docs keeping build work bounded.

## In Scope

- create one concept page about slice docs as a control surface
- connect it to the request boundary episode pages

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should explain how slice docs bound build work

## Main Business Rules

- slice docs should keep build scope narrow
- slice docs should state evidence expectations
- slice docs should not become implementation code

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/057-slice-docs-keep-build-bounded.md` exists
- the home page links to the page
- the concepts index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the concepts index lists the page

## Scenario Definition

1. open the concept page
2. follow links to the related episode and note pages

## Done Criteria

- the concept page exists and is linked
- the page reinforces bounded build work
- the change is represented in `work/changes/0031/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid making slice docs sound like code
