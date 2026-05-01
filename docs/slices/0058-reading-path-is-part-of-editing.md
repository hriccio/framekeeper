# Slice 0058 - Reading Path Is Part Of Editing

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

Add a concept page that says the reading path is part of editing, not an afterthought.

## In Scope

- create one concept page about reading paths
- link it to the episode and note pages that motivate it

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should explain why editing includes navigation

## Main Business Rules

- editing includes the path a reader follows
- the page should not become a navigation tutorial
- the reading path should stay visible and intentional

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/reading-path-is-part-of-editing.md` exists
- the home page links to the page
- the concepts index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the concepts index lists the page

## Scenario Definition

1. open the concept page
2. follow links to the episode and note pages it references

## Done Criteria

- the concept page exists and is linked
- the page preserves the editing-path boundary
- the change is represented in `work/changes/0015/implementation.md`

## Resolved Design Decisions

- keep the page narrow
- avoid turning it into a browsing theory document

