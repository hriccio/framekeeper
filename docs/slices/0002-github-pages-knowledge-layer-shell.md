# Slice 0002 - GitHub Pages Knowledge Layer Shell

## Status

Accepted.

## Selected Pack

- documentation-first, no runtime pack change

## Runtime Targets

- GitHub Pages from `docs/`
- local markdown browsing and link checking

## Architecture Mode

- static markdown site shell
- manual content authoring first, automation later

## Intent

Create the smallest publishable knowledge layer for `@umoutrohenrique`:

```text
docs/index.md -> docs/episodes/index.md -> docs/concepts/index.md -> docs/references/index.md -> docs/episodes/001-template.md
```

The site should be easy to browse locally and easy to publish through GitHub
Pages without extra infrastructure.

## In Scope

- create a home page
- create episodes, concepts, and references indices
- create one episode template
- add clear markdown navigation between those pages
- explain the GitHub Pages publishing path in `readme.md`

## Use-Case Contract

- input: manually authored markdown content
- output: a browsable GitHub Pages site root under `docs/`
- behavior: navigation should work with relative links in local markdown and on GitHub Pages
- behavior: raw transcripts remain outside the published site unless intentionally exposed later

## Main Business Rules

- markdown is the source of truth
- raw content stays separate from refined content
- no custom domain is required
- no automation or CMS is required for the first slice

## Required Ports

- none

## Out Of Scope

- custom domain setup
- CMS/editor tooling
- search
- database-backed content management
- transcript automation
- publication automation

## Candidate Acceptance Criteria

- `docs/index.md` exists
- `docs/episodes/index.md` exists
- `docs/concepts/index.md` exists
- `docs/references/index.md` exists
- `docs/episodes/001-template.md` exists
- navigation links are present and local-link friendly
- `readme.md` explains how to publish from GitHub Pages

## Initial Test Plan

- a test verifies the expected docs files exist
- a test verifies the root index links to the section indices

## Scenario Definition

1. open `docs/index.md`
2. follow the navigation to the section indices
3. open the episode template

Each step should be possible without additional tooling.

## Done Criteria

- the docs site shell exists and is navigable
- the README explains the publishing path
- tests confirm the required documents exist and are linked
- the change is represented in `work/changes/0002/implementation.md`

## Resolved Design Decisions

- use `docs/` as the GitHub Pages publishing root
- keep the site markdown-first rather than adopting a site generator
- keep raw transcripts outside the published site for now
- leave automation for later slices

