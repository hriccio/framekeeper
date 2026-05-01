# Slice 0011 - GitHub Pages Is Enough For Now

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

Add an episode page that keeps the site grounded on GitHub Pages without adding
custom hosting complexity.

## In Scope

- create one episode page about the hosting decision
- link it to the GitHub Pages reference page

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should keep the publishing path simple and versioned

## Main Business Rules

- GitHub Pages is the current publishing target
- no custom domain is required for the current scope
- the episode page should avoid turning into deployment instructions

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/005-github-pages-is-enough-for-now.md` exists
- the home page links to the page
- the episodes index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the episodes index lists the page

## Scenario Definition

1. open the episode page
2. follow the link to the GitHub Pages reference page

## Done Criteria

- the episode page exists and is linked
- the page keeps the hosting decision simple
- the change is represented in `work/changes/0006/implementation.md`

## Resolved Design Decisions

- keep the page focused on the current hosting choice
- do not use the page to justify unrelated infrastructure work

