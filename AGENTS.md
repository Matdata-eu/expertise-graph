# Agent Skills For This Repository

## Purpose

This repository is a Logseq-authored expertise graph that is exported to RDF, cleaned, validated with SHACL, and published as a website, RDF dataset, and CV.

## Page Types

Choose the page type before writing content. In this repository, the main authoring patterns are:

1. `[[Project]]` for software systems, libraries, utilities, platforms, or internal initiatives.
2. `[[Talk]]` for conference talks, workshops, courses, webinars, and presentations.
3. `[[Technique]]` for technologies, methods, formats, frameworks, and tools.
4. `[[Role]]` for professional roles and responsibilities.
5. `[[Job]]` for employment or freelance periods tied to companies and roles.

## When Adding Project Pages

1. Read [README.md](README.md) first to confirm the data model and validation workflow.
2. Read the target project's README or source repository before writing the page so the description and techniques come from project metadata, not guesswork.
3. Create one markdown page per project under `pages/` using this minimum shape:

```markdown
public:: true
type:: [[Project]]
description:: Brief factual description
has-category:: Existing project category
has-tagged-techniques:: #ExistingTechnique, #[[Existing Technique]]
has-tagged-roles:: #Developer
has-linked-projects:: #[[Related Project]]
is-featured:: No
during-job:: #[[Job: Independent railway data freelancer]]
external-link:: https://example.org
```

## When Adding Talk Pages

1. Use `[[Talk]]` when the page is primarily about delivering content to an audience rather than building software.
2. Keep supporting bullet points, links to slide decks, and event references below the page properties.
3. Use this minimum shape:

```markdown
public:: true
type:: [[Talk]]
format:: Conference
audience-size:: 100
is-featured:: No
external-link:: https://example.org
year:: 2026
during-job:: #[[Job: Independent railway data freelancer]]
```

## When Adding Technique, Role, Or Job Pages

Use these compact templates when vocabulary is missing and genuinely needs to be created:

```markdown
public:: true
type:: [[Technique]]
self-estimated-proficiency:: Competent
is-featured:: No
has-category:: Programming languages
```

```markdown
public:: true
type:: [[Role]]
self-estimated-proficiency:: Competent
is-featured:: No
has-category:: Data & IT role
```

```markdown
type:: [[Job]]
started-on:: 2025-01
ended-on::
has-duration:: tbd
at-company:: #[[Company Name]]
description:: Brief factual description
has-linked-roles:: #Developer
```

## Vocabulary Rules

1. Reuse existing techniques, roles, categories, jobs, companies, and page types whenever possible.
2. If a referenced technique or role does not exist yet, add its own page under `pages/` using the correct entity template before using it.
3. Do not invent new category labels if an existing one already fits.
4. For freelance open source and side projects in the current period, default to `during-job:: #[[Job: Independent railway data freelancer]]` unless the user explicitly ties the work to another job.
5. When a page is about a workshop, course, or presentation, prefer `[[Talk]]` over `[[Project]]`.

## Good Sources For Cross-Links

1. Nearby project pages with similar domain or tooling.
2. Existing talk, workshop, or open source pages in the semantic tooling area.
3. The target repository README for public links, deployment info, and scope.

## Validation

After edits, run the local validation workflow from the repository root:

```powershell
python .\kg-actions\clean-graph.py
python .\kg-actions\validate-graph.py
python .\cv\complete-cv.py
```

If broader end-to-end verification is needed, use:

```powershell
.\run-pipeline.ps1
```

Do not finish after writing markdown only; the graph is schema-validated and broken references can surface only during validation.