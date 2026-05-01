# Slice 0045 - Titles Should Match The Idea

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

Add an episode page that says titles should match the idea of the page.

## In Scope

- create one episode page about titles
- link it back to the concept and note pages that support the rule

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain why titles need to fit the content

## Main Business Rules

- titles should be honest
- titles should help readers predict the page
- the page should not become a title-writing manual

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/018-titles-should-match-the-idea.md` exists
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
- the page reinforces honest title usage
- the change is represented in `work/changes/0013/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a copywriting guide

