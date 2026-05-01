# Slice 0067 - Raw Evidence Is Not The Site

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

Add a concept page about raw evidence staying separate from the public site.

## In Scope

- create one concept page about raw evidence not becoming the site

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should explain why source material stays in the working layer

## Main Business Rules

- raw evidence supports the site but does not replace it
- the public layer should remain refined
- the page should stay short and reusable

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/raw-evidence-is-not-the-site.md` exists
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
- the page reinforces the raw/public boundary
- the change is represented in `work/changes/0017/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid making it a storage guide
