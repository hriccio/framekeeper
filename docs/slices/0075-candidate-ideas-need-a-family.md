# Slice 0075 - Candidate Ideas Need A Family

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

Add an episode page that says candidate ideas need a page family.

## In Scope

- create one episode page about candidate ideas needing a family
- link it to the concept and note pages that support family assignment

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain why candidate ideas need a destination

## Main Business Rules

- candidate ideas should be assigned to a page family
- the draft should not stay ambiguous for long
- the page should not become a taxonomy lecture

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/030-candidate-ideas-need-a-family.md` exists
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
- the page reinforces family assignment
- the change is represented in `work/changes/0019/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into an editorial taxonomy guide
