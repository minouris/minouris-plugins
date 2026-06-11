# Term Indexing and Glossary Standards

**This file is loaded when: You need guidance on organizing, indexing, and presenting domain terms in a structured glossary format.**

---

# Embedded Rules

## Literal Specification Compliance (from /src/claude/rules/literal-specification.md)

**Term Entry Template is Expressly Specified - Compliance is MANDATORY:**

**MUST:**
- Reproduce term entries character-for-character to the specified template
- Use only the fields and sections in the specification
- Follow the exact heading level, spacing, and content order
- Include all required fields: Captured, Short description, Sources table, Referenced By

**MUST NOT:**
- Add fields to term entries beyond what is specified
- Add summary sections or metadata not in specification
- Enhance term entries with additional context or navigation
- Modify the template structure "for convenience"
- Include explanatory or contextual sections not in template

---

## Markdown Formatting Standards (from /.claude/rules/markdown-formatting.md)

### Filename Conventions (MANDATORY)

**MUST:**
- Use lower-snake-case for all term index filenames (e.g., `index_terms.md`, `index_terms_auth_con.md`)
- Use `.md` extension for all Markdown files

**MUST NOT:**
- Use kebab-case (e.g., `index-terms.md`)
- Use camelCase (e.g., `indexTerms.md`)
- Use PascalCase (e.g., `IndexTerms.md`)
- Use spaces in filenames

---

## Overview

When you maintain terms for a topic, organize them into a hierarchical glossary structure with:
- Individual term entries using a standardized template
- Multiple index files when exceeding size limits
- A central index that points to all verified terms
- Bidirectional links between terms, findings, and sources

---

## Sources vs. Referenced By: Critical Distinction

When maintaining term entries, understand the difference between these two sections:

**Sources table** (defines the term):
- Canonical/authoritative documents that *define* the term
- Official documentation, specifications, standards
- The authoritative source of truth for the term definition
- Example: [Official GraphQL Specification](https://spec.graphql.org/)

**Referenced By section** (uses the term):
- Facts, findings, and research that *reference or use* the term
- Evidence that this term is relevant to the topic
- Where the term appears in your analysis
- Example: FINDING-2026-03-22-1 - Implementation uses GraphQL

These are distinct purposes and must not be confused. The Sources table proves the term is real and well-defined; Referenced By proves it's relevant to your analysis.

---

## Term Entry Template

When you create a term entry, use this exact structure:

```markdown
## <Term Name>

**Captured:** YYYY-MM-DD HH:MM

<Short description - maximum 3 sentences summarizing the term>

### Sources

| Source | Status | Verification |
|--------|--------|---------------|
| [Source Name](link/to/source.md) | VERIFIED / UNVERIFIED / PENDING | [Verification](verification/link.md) |
| [Another Source](link/to/source.md) | VERIFIED | [Verification](verification/link.md) |

### Description

<Long description of the term, including:
- Detailed definition
- Key characteristics
- Scope and boundaries
- How it relates to the topic>

### See Also

- [Related Term 1](#related-term-1)
- [Related Term 2](#related-term-2)
- [Concept Name (not yet defined)](undefined-concept)

### Referenced By

- [FINDING-2026-03-22-1](../facts/topic-facts.md#finding-2026-03-22-1) - Finding Title
- [FINDING-2026-03-22-4](../facts/topic-facts.md#finding-2026-03-22-4) - Another Finding
```

### Field Requirements

When you create a term entry, populate these fields:

- **Term Name (H2)**: The semantic concept label (1-4 words typically)
- **Captured**: Timestamp when term was created (YYYY-MM-DD HH:MM format)
- **Short description**: 1-3 sentences summarizing what this term is; appears in central index
- **Sources table**: List canonical/authoritative sources that *define* this term (official documentation, specifications, standards). Do NOT list where the term is used; list only definition sources with verification status.
- **Description**: Complete definition with context, characteristics, scope boundaries, and topic relationships
- **See Also**: Links to related terms (use internal anchor links for terms in same file; use relative paths for other files)
- **Referenced By**: Backlinks to facts that use or reference this term

---

## Term Index Files

### File Organization and Naming

When you create term index files, follow this structure:

**Single index file (for topics with ≤500 lines):**
```
.memory/[topic]/[topic]-terms.md
```

**Multiple index files (for topics exceeding 500 lines):**
```
.memory/[topic]/[topic]-terms-index-aaa-bbb.md
```

Where:
- `aaa` = first 3 letters of the first term in the file
- `bbb` = first 3 letters of the last term in the file
- Example: `terms-index-hal-ove.md` (Hallucination → Overeagerness)

### File Structure

When you organize terms in an index file, structure it like this:

```markdown
# [Topic Name] Terms

**Last Updated:** YYYY-MM-DD HH:MM
**Verified Terms:** N
**Pending Terms:** N

---

## Table of Contents

- [Term 1](#term-1)
- [Term 2](#term-2)
- [Term 3](#term-3)

---

## Term 1

**Captured:** YYYY-MM-DD HH:MM

Short description here.

### Sources

| Source | Status | Verification |
|--------|--------|---------------|
| ... |

### Description

...

### See Also

...

### Referenced By

...

---

## Term 2

...
```

### Size Management

**Monitor term index file size:**
- **Maximum:** 500 lines per file
- **Action trigger:** When you would add a term that would exceed this limit

**When approaching the 500-line limit, execute this process:**

1. Identify terms that should move to a new file (use alphabetical midpoint)
2. Create new index file: `.memory/[topic]/[topic]-terms-index-[first-3]-[last-3].md`
3. Move identified terms to new file
4. Update central index (`index-terms.md`) with both files
5. Add navigation links between index files

**Alphabetical Range Selection:**

Keep range spans natural and balanced:
- Don't split at arbitrary points
- Keep ranges that group related terms together when possible
- Divide at letters that result in ±1-2 terms per page

**Example division for 20+ terms:**
- `terms-index-aut-con.md` (Authentication → Context)
- `terms-index-des-jso.md` (Design → JSON)
- `terms-index-mem-pat.md` (Memory → Pattern)
- `terms-index-sta-zap.md` (Stateful → Zapping)

---

## Central Index: index-terms.md

When you maintain terms for a topic, create and maintain a central index file:

**Location:**
```
.memory/[topic]/index-terms.md
```

**Structure:**

```markdown
# Terms Index

| Term | Short Description |
|------|-------------------|
| [Term Name](path/to/terms-file.md#term-name) | Short description (max 3 sentences) |
| [Another Term](path/to/terms-file.md#another-term) | Another short description |
```

### Central Index Requirements

**MUST:**
- List only VERIFIED terms in this index
- Include short description (max 3 sentences) from term entry
- Link to term location in appropriate index file
- Maintain alphabetical order
- Include H1 title and two-column table only

**MUST NOT:**
- Include unverified or pending terms
- Add metadata, topic fields, or verification status sections
- Add index file lists, verification sections, or other organizational structure
- Use this file to store full term definitions (use term index files)

---

## Sources Table Requirements

The Sources table in each term entry must contain canonical/authoritative sources that *define* the term, not locations where it is used.

### Source Types by Term Category

**For Industry Standard Terms:**
- Official specification documents (RFC, W3C, OASIS, ISO, IEEE)
- Official standards glossaries
- Consensus definitions in authoritative technical documentation
- Example source: https://tools.ietf.org/html/rfc7231 (defines REST API)

**For Official Third-Party Terms:**
- Official product/service documentation
- Official API references
- Official language/framework documentation
- Example source: https://docs.github.com/rest (GitHub REST API definition)

**For Internal/Project-Specific Terms:**
- Project design documents and specifications
- Project documentation establishing the term
- Team documentation or conventions
- Example source: Project architecture document defining internal concepts

### Source Table Format

Structure the Sources table like this:

```markdown
### Sources

| Source | Status | Verification |
|--------|--------|--------------|
| [Official Specification](https://official.spec/ref) | VERIFIED | Verified 2026-03-23 against section 3.1 |
| [Official Documentation](https://docs.example.com) | VERIFIED | Verified 2026-03-23 against API reference |
```

- **Source**: Link to the authoritative definition document or specification
- **Status**: VERIFIED (term confirmed to match source), UNVERIFIED (needs checking), or DISPUTED (conflicting definitions)
- **Verification**: Date and specific section/reference confirming the definition

### MUST NOT Put in Sources Table

Do NOT include in the Sources table:
- ❌ Facts or findings that use the term
- ❌ Internal project code or analysis files
- ❌ Facts with IDs (FINDING-XXXX) - those go in "Referenced By"
- ❌ Multiple locations where the term appears
- ❌ Sources that reference the term but don't define it

### Verification Fast Path: Terms from Official Documentation

When facts are extracted from official documentation, that documentation provides authoritative term definitions. This creates an efficient verification workflow:

**When verifying terms sourced from official documentation:**
1. The official documentation cited in the Sources table IS the canonical definition
2. Invoke `/verify-analysis term [topic] [subtopic] [term-id]` skill
3. Skill verifies that terminology against other official sources (alternate documentation, related specifications, cross-references)
4. Skill confirms the term is used consistently across the official documentation
5. Skill marks as VERIFIED once usage consistency is confirmed across sources
6. Skill creates verification working document with verbatim evidence

**Example verification:**
- Term "Pull Request" with source: https://docs.github.com/pull-requests
- Invoke: `/verify-analysis term github-api "Pull Request"`
- Skill checks GitHub REST API docs, GitHub GraphQL API docs, and other official GitHub documentation
- If usage is consistent across these official sources: Marked VERIFIED
- Verification working document: "Verified 2026-03-23 across GitHub REST, GraphQL, and main documentation"

This fast-path workflow leverages the official documentation's authority while maintaining verification rigor through the `/verify-analysis term` skill.

---

When you maintain terms, ensure complete traceability:

### Terms → Findings (Backlinks)

In each term entry, maintain a "Referenced By" section:

```markdown
### Referenced By

- [FINDING-2026-03-22-1](../facts/topic-facts.md#finding-2026-03-22-1) - Finding demonstrates this term
- [FINDING-2026-03-22-4](../facts/subtopic/topic-subtopic-facts.md#finding-2026-03-22-4) - Another finding using term
```

**Update "Referenced By" when:**
- A new fact introduces or uses this term
- A fact is archived (remove from backlinks)
- Cross-references are added or removed

### Findings → Terms (Forward Links)

In fact entries, include term references:

```markdown
**Introduces term:** TERM-[topic]-[YYYY-MM-DD]-1

**Uses terms:** TERM-[topic]-[YYYY-MM-DD]-3, TERM-[topic]-[YYYY-MM-DD]-5
```

### Transitive Fact References Through Term Hierarchy

When a term extends or references another term (establishing a hierarchical relationship), facts that reference the child term automatically also reference the parent term.

**Example:** If GitHub REST API has "See Also: [GitHub API](#github-api)" establishing it as a child/implementation of GitHub API, then any fact referencing GitHub REST API also implicitly references GitHub API.

**When updating "Referenced By":**
- Include facts that reference this term directly
- Include facts that reference any child term (as child terms imply parent term usage)
- Mark transitive references by adding a note: `(via GitHub REST API)`

**Example:**
```markdown
### Referenced By

- [FINDING-2026-03-22-1](../facts/topic-facts.md#finding-2026-03-22-1) - Direct reference to GitHub API
- [FINDING-2026-03-22-3](../facts/topic-facts.md#finding-2026-03-22-3) - Via GitHub REST API
- [FINDING-2026-03-22-5](../facts/topic-facts.md#finding-2026-03-22-5) - Via GitHub GraphQL API
```

---

## Term Verification Workflow

When you verify terms, update their status:

### Before Verification

**Status:** UNVERIFIED
- Term appears in index files but NOT in central index
- Included in "Pending Verification" section if applicable

### During Verification

**Status:** PENDING
- Verification workflow is in progress
- Source materials are being checked
- Scope and boundaries are being validated

### After Verification

**Status:** VERIFIED
- Term now appears in central `index-terms.md`
- Verification link points to completed verification document
- Short description confirmed accurate

**Mark verification in Sources table:**
```markdown
| [Source Document](link/to/source.md) | VERIFIED | [Verified on 2026-03-22 by Source](verification/source-link.md) |
```

---

## Common Patterns

### Single-Level Hierarchy (Small Topics)

For topics with few terms (≤ 5-10 terms):
```
.memory/[topic]/[topic]-terms.md        (single file, ≤500 lines)
.memory/[topic]/index-terms.md          (central index)
```

### Two-Level Hierarchy (Medium Topics)

For topics with moderate terms (50-100 terms):
```
.memory/[topic]/[topic]-terms-index-aut-key.md    (terms A-K)
.memory/[topic]/[topic]-terms-index-lea-zap.md    (terms L-Z)
.memory/[topic]/index-terms.md                     (central index)
```

### Three-Level Hierarchy (Large Topics)

For topics with many terms (100+ terms):
```
.memory/[topic]/[topic]-terms-index-aut-con.md    (terms A-C)
.memory/[topic]/[topic]-terms-index-des-ini.md    (terms D-I)
.memory/[topic]/[topic]-terms-index-jso-ove.md    (terms J-O)
.memory/[topic]/[topic]-terms-index-pat-zap.md    (terms P-Z)
.memory/[topic]/index-terms.md                     (central index)
```

---

## MUST/MUST NOT Summary

**When creating term index files, you MUST:**
- Use alphabetical ordering (primary sort key)
- Include Table of Contents for files with 10+ terms
- Use H2 heading for each term
- Include all required fields (Captured, Sources, Description, See Also, Referenced By)
- Keep line count under 500 per file
- Create new file when approaching limit
- Update central index after new term verification

**When maintaining terms, you MUST:**
- Only include VERIFIED terms in central index
- Maintain bidirectional links between terms and facts
- Update "Referenced By" when facts change
- Include transitive fact references when a term extends another term
- Mark transitive references with the child term that mediates the reference
- Use correct naming convention for multi-file organization

**When verifying terms, you MUST:**
- Verify canonical definition sources before marking term as VERIFIED
- Confirm term definition matches authoritative source exactly
- For official/industry standard terms: Link to official specification or documentation
- For internal terms: Cite project documentation that establishes the term
- Verify scope boundaries align with authoritative definition
- Include verification dates and source references

**When verifying terms, you MUST NOT:**
- Mark terms as VERIFIED without completing verification workflow
- Include unverified terms in central index
- Leave incomplete Source entries
- Create bidirectional links until term is verified
- Mark terms VERIFIED if no authoritative source can be found (archive as disputed instead)

**When managing hierarchical relationships, you MUST:**
- Update parent term "Referenced By" when child terms are referenced by facts
- Add transitive references with notation: `(via Child Term Name)`
- Ensure all parent terms reflect usage through their children

**When organizing terms, you MUST NOT:**
- Exceed 500 lines per index file without creating new file
- Use arbitrary term splitting points
- Leave broken links between index files
- Omit verified terms from central index
- Forget transitive references when updating "Referenced By" sections

**When sourcing and verifying terms, you MUST:**
- Consult authoritative sources (industry standards, official documentation) before creating terms
- Cite canonical definition sources in the Sources table (not usage references)
- Verify that industry standard or official terms exist before creating internal terms
- Link to authoritative definitions that establish term validity
- Distinguish between definition sources (Sources) and usage references (Referenced By)
- For internal terms: Cite project documentation that establishes the term
- Update verification status with date and specific source section

**When sourcing and verifying terms, you MUST NOT:**
- Create terms that duplicate existing industry standard or official terminology
- Put facts or findings in the Sources table (they belong in Referenced By)
- Include locations where the term appears instead of where it is defined
- Mark terms VERIFIED without authoritative source documentation
- Confuse definition sources (Sources table) with usage references (Referenced By section)
