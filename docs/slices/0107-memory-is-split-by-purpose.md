# Slice 0107 - Memory Is Split By Purpose

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

Add a concept page about memory being split by purpose.

## In Scope

- create one concept page about memory roles in the repository

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should explain why different memory types stay separate

## Main Business Rules

- raw evidence, loop history, and published pages have different jobs
- each memory type should stay in its own place
- the page should stay short and reusable

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/memory-is-split-by-purpose.md` exists
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
- the page reinforces memory separation
- the change is represented in `work/changes/0025/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a storage architecture note
