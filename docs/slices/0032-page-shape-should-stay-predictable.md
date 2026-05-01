# Slice 0032 - Page Shape Should Stay Predictable

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

Add a concept page that preserves predictable page shape across the site.

## In Scope

- create one concept page about page shape
- link it to the episode pages that use the same structure

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should describe why page shape matters

## Main Business Rules

- page shape should remain predictable
- structure should support scanning and editing
- the page should not become a general formatting policy

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/page-shape-should-stay-predictable.md` exists
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
- the page preserves the page-shape boundary
- the change is represented in `work/changes/0010/implementation.md`

## Resolved Design Decisions

- keep the page about shape, not style aesthetics
- avoid making it a markdown syntax tutorial

