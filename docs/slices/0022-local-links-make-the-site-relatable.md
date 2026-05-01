# Slice 0022 - Local Links Make The Site Relatable

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

Add a concept page that explains why local links keep the site easy to browse
and maintain.

## In Scope

- create one concept page about local links
- link it back to the episode and note pages that use local references

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should explain why relative links matter

## Main Business Rules

- local links should work in GitHub Pages and in a local browser
- navigation should remain simple and inspectable
- the page should not become a markdown tutorial

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/local-links-make-the-site-relatable.md` exists
- the home page links to the page
- the concepts index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the concepts index lists the page

## Scenario Definition

1. open the concept page
2. follow the links to the episode and note pages it references

## Done Criteria

- the concept page exists and is linked
- the page preserves the local-link rule
- the change is represented in `work/changes/0008/implementation.md`

## Resolved Design Decisions

- keep the page focused on relative navigation
- avoid duplicating the site shell guidance

