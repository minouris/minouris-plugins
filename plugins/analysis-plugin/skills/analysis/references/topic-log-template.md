# Topic Log Bootstrap Template

**This file provides the template for `[topic-slug]-log.md` files that record research operations and session continuity for a topic.**

---

# Embedded Rules

## Literal Specification Compliance (from /src/claude/rules/literal-specification.md)

When you create a topic log from this template:

**MUST:**
- Implement exactly what is specified in the template
- Reproduce the template structure with all sections
- Use the template format precisely (heading levels, spacing, content order)
- Implement only the sections specified in this template

**MUST NOT:**
- Add sections beyond the template specification
- Add metadata or organizational elements not in the template
- Modify heading levels or section order
- Include explanatory content beyond the template

---

# Topic Log Template

Use this template to create `${workspace}/.memory/[topic-slug]/[topic-slug]-log.md`:

```markdown
# [Topic Name] - Operation Log

**Topic:** [topic-slug]
**Session started:** YYYY-MM-DD

## Operations

### OP-YYYY-MM-DD-NNN: [Operation name/title]

**Operation type:** [Type - e.g., "Session initialization", "Fact capture", "Term extraction", "Verification", "Index update"]

**Files created/modified:**
- `[filename]` - [Description]

**Key output:**
- [Bullet point describing outcome or findings created]

**Timestamp:** YYYY-MM-DD

---
```

---

# Template Guidelines

## Header Section

Provide topic identification and session information:

- **Topic:** Topic slug (e.g., `github-api`)
- **Session started:** Date research began on this topic (YYYY-MM-DD format)

## Operations Section

Record each significant operation chronologically:

### Operation Entry Format

- **OP-YYYY-MM-DD-NNN**: Unique operation identifier (date-based + incrementing sequence)
- **Operation type**: Category of work (Session initialization, Fact capture, Term extraction, Verification, Index update, etc.)
- **Files created/modified**: List files affected by this operation with brief descriptions
- **Key output**: Bullet points describing what this operation produced (findings, terms, etc.)
- **Timestamp**: When operation was completed (YYYY-MM-DD)

Add separator (`---`) between operations.

---

# Usage in Topic Bootstrap

When the analysis skill's topic bootstrap feature creates a new topic:

**MUST:**
1. Create `[topic-slug]-log.md` using this template
2. Fill header with topic slug and today's date as session start
3. Initialize with bootstrap operation entry documenting directory and file creation
4. Use OP-YYYY-MM-DD-001 as first operation ID

**MUST NOT:**
- Add sections beyond those in this template
- Modify the template structure
- Add metadata not specified in the template

---

# Operation Type Reference

Common operation types for consistent categorization:

- **Session initialization**: First load of topic, bootstrap of structure
- **Fact capture**: Capturing new findings in fact file
- **Term extraction**: Extracting semantic terms from findings
- **Term verification**: Verifying extracted terms with external sources
- **Fact verification**: Verifying facts against authoritative sources
- **Index update**: Updating topic index with new findings or status changes
- **Disproven archive**: Moving findings to disproven archive
