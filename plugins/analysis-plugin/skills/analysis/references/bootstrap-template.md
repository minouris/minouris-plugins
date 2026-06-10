# Knowledge Base Index Bootstrap Template

**This file provides the template for `knowledge-base-index.md` files that bootstrap new knowledge base instances.**

---

# Embedded Rules

## Literal Specification Compliance (from /src/claude/rules/literal-specification.md)

When you create a knowledge base index from this template:

**MUST:**
- Implement exactly what is specified in the template
- Reproduce the template structure with all sections
- Use the template format precisely (heading levels, spacing, content order)
- Implement only the sections specified in this template

**MUST NOT:**
- Add sections beyond the template specification
- Add metadata or organizational elements not in the template
- Add summary sections or additional navigation
- Include explanatory content beyond the template

---

# Bootstrap Template

Use this template to create `${workspace}/.memory/knowledge-base-index.md`:

```markdown
# Knowledge Base Index

**Last Updated:** YYYY-MM-DD

---

## Quick Search Guide

Use this index to locate knowledge relevant to your task:

| If you need... | See Topic | Key Findings |
|---|---|---|
| [Add examples for your topics] | [topic-link](#topic-slug) | [Key finding IDs or descriptions] |

---

## Topic Directories

### [topic-name]

**Knowledge Summary:**

[1-2 paragraph summary of the topic's knowledge, describing what makes it authoritative for this domain and what problems it helps solve]

**Quick Links:**
- Full index: [topic-slug-index.md]([topic-slug]/[topic-slug]-index.md)
- Main facts: [topic-slug-facts.md]([topic-slug]/[topic-slug]-facts.md)
- [Additional quick links specific to topic structure]

**Research Areas:**
- [Research Area Name] ([N] verified findings)
- [Research Area Name] ([N] verified findings, [M] disproven)

**Key Concepts:**
- [Concept Name] — Short definition of the concept (1-2 sentences)
- [Concept Name] — Short definition of the concept (1-2 sentences)

---

## Central Index Maintenance Log

| Date | Topic | Action | Details |
|---|---|---|---|
| YYYY-MM-DD | All | knowledge-base-index.md created | Initial knowledge base bootstrap |

---
```

---

# Template Guidelines

## Topic Sections

For each topic in your knowledge base, create a topic section with:

1. **Knowledge Summary** (required): 1-2 paragraphs describing what the topic covers, why it's authoritative, and what problems it helps solve
2. **Quick Links** (required): Paths to key files (index, facts, etc.) specific to your topic structure
3. **Research Areas** (required): List of research areas within the topic with verification counts
4. **Key Concepts** (required): Bulleted list of key terms with 1-2 sentence definitions

## Quick Search Guide

Create table rows for common queries users might have about your knowledge base. Map queries to topics that address them.

## Maintenance Log

Record when the knowledge base was created and when significant updates occur (new topics, major verification cycles).

---

# Usage in Bootstrap Feature

When the analysis skill's bootstrap feature creates a new knowledge base:

**MUST:**
1. Create `.memory` directory if it doesn't exist
2. Create `knowledge-base-index.md` using this template as the structure foundation
3. Populate Quick Search Guide with your project's topic mappings
4. Populate Topic Directories with your research topics (following this template exactly)
5. Initialize Maintenance Log with creation date and initial topics
6. All other sections remain in place as-is

**MUST NOT:**
- Add sections beyond those in this template
- Modify the template structure
- Add metadata not specified in the template
