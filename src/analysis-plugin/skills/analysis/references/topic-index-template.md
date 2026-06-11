# Topic Index Bootstrap Template

**This file provides the template for `[topic-slug]-index.md` files that organize and index findings for a research topic.**

---

# Embedded Rules

## Literal Specification Compliance (from /src/claude/rules/literal-specification.md)

When you create a topic index from this template:

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

# Topic Index Template

Use this template to create `${workspace}/.memory/[topic-slug]/[topic-slug]-index.md`:

```markdown
# [Topic Name] - Index

## Knowledge Summary

**Overview:** [1-2 sentence overview of what this topic covers]

**Research Domains:** [Comma-separated list of primary research domains within topic]

**Core Terminology:** [Comma-separated list of key concepts/terms]

**Verification Status:**
- Verified: [N] findings
- Unverified: [N] findings
- Disproven: [N] findings
- **Status:** [Current research status - nascent, active, paused, completed]

**Total Findings:** [N]

**Last Updated:** YYYY-MM-DD

---

**Topic:** [topic-slug]

## Fact Files

- `[topic-slug]-facts.md` - [Description of main fact file contents]
  - Companion disproven: `[topic-slug]-disproven.md` (pending or exists)

## Findings

| Finding | Topic | Name | Terms |
|---------|-------|------|-------|
| [FINDING-YYYY-MM-DD-N](#finding-yyyy-mm-dd-n) | [Brief topic description] | [Finding name] | [term1](#term1), [term2](#term2) |
```

---

# Template Guidelines

## Knowledge Summary

Provide a high-level overview of the topic:

- **Overview**: 1-2 sentences describing the research focus
- **Research Domains**: Primary areas of investigation within the topic (comma-separated)
- **Core Terminology**: Key concepts and terms used throughout research
- **Verification Status**: Current state of findings (counts and status)
- **Total Findings**: Total number of fact findings captured
- **Last Updated**: Date the index was last updated (YYYY-MM-DD)

## Fact Files Section

List all fact files in the topic directory:

- Primary fact file: `[topic-slug]-facts.md` with description
- Note companion disproven file status (pending if not yet created)

## Entries

Table with columns:
- **Finding**: Finding identifier (FINDING-YYYY-MM-DD-N) linked to the finding in the fact file
- **Topic**: Brief category for what the finding covers
- **Name**: Short descriptive name of the finding
- **Terms**: Comma-separated list of relevant semantic terms (optional, populated as terms are defined and linked)

Update this table whenever facts are added or verified. Link terms to their definitions in the topic's term index file.

---

# Usage in Topic Bootstrap

When the analysis skill's topic bootstrap feature creates a new topic:

**MUST:**
1. Create `[topic-slug]-index.md` using this template
2. Fill Knowledge Summary with research scope and status
3. Initialize Fact Files section with planned fact file
4. Initialize empty Findings table (populate as findings are captured)
5. Leave Terms column empty until terms are extracted and defined

**MUST NOT:**
- Add sections beyond those in this template
- Modify the template structure
- Add metadata not specified in the template
