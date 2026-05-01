# Slice 0003 - Knowledge Layer Content Seed

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

Add the first concrete content seed to the knowledge layer:

- one episode page
- one concept page
- one reference page

The pages should demonstrate how the site is meant to hold structured ideas
without depending on automation.

## In Scope

- create one example episode page beyond the template
- create one example concept page
- create one example reference page
- link the home page and indices to the seeded content

## Use-Case Contract

- input: manually authored markdown
- output: navigable knowledge-layer pages under `docs/`
- behavior: the example pages should reference each other with local links
- behavior: the site should still keep raw transcripts out of the published tree

## Main Business Rules

- markdown is the source of truth
- refined content lives separately from raw evidence
- reference pages are curated, not generated
- no automation or CMS is required

## Required Ports

- none

## Out Of Scope

- transcript ingestion automation
- content generation automation
- publishing automation
- database support
- search support

## Candidate Acceptance Criteria

- `docs/episodes/001-contexto-em-ia.md` exists
- `docs/concepts/contexto-em-ia.md` exists
- `docs/references/github-pages.md` exists
- the home page links to those pages
- the section indices list those pages

## Initial Test Plan

- a test verifies the seeded pages exist
- a test verifies the home page links to the seeded pages
- a test verifies the section indices list the seeded pages

## Scenario Definition

1. open the home page
2. open the seeded episode page
3. follow the concept and reference links

## Done Criteria

- the knowledge layer has a first content seed
- the site still behaves as a simple markdown-first GitHub Pages tree
- tests confirm the seed and navigation
- the change is represented in `work/changes/0003/implementation.md`

## Resolved Design Decisions

- seed the content with a single representative episode on context and AI
- use local markdown links between the seeded pages
- keep the example content small enough to edit manually

