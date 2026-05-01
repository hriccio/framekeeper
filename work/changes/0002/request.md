# Request

- Change: `0002`
- Date: 2026-05-01

## Request Boundary

Build the first GitHub Pages-ready knowledge layer for `@umoutrohenrique`:

```text
docs/ index -> episodes index -> concepts index -> references index -> episode template
```

The request is for a minimal, markdown-first site shell that can be published
from `docs/` without custom domain setup or CMS machinery.

## Success Expectations

- the site has a home page under `docs/index.md`
- the site has section indices for episodes, concepts, and references
- there is at least one episode template document
- navigation between the pages is clear and local-link friendly
- the repository README explains how to publish through GitHub Pages

## Out Of Scope

- custom domain setup
- CMS or editorial tooling
- database-backed content management
- search indexing
- static-site-generator complexity
- transcript automation
- publication automation

