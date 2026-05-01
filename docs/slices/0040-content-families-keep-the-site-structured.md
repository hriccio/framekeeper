# Slice 0040 - Content Families Keep The Site Structured

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

Add an episode page that explains how content families keep the site
structured.

## In Scope

- create one episode page about page families
- link it back to the concept and note pages that define the families

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should describe why the page families stay distinct

## Main Business Rules

- episodes, concepts, references, and notes have different jobs
- structure should help readers understand those jobs
- the page should not become a taxonomy lecture

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/016-content-families-keep-the-site-structured.md` exists
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
- the page reinforces the family structure boundary
- the change is represented in `work/changes/0012/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a repository ontology guide

