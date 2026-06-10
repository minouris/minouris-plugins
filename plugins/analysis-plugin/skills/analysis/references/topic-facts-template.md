# Topic Facts Bootstrap Template

**This file provides the template for `[topic-slug]-facts.md` files that contain research findings for a topic.**

---

# Embedded Rules

## Literal Specification Compliance (from /src/claude/rules/literal-specification.md)

When you create a topic facts file from this template:

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

# Topic Facts Template

Use this template to create `${workspace}/.memory/[topic-slug]/[topic-slug]-facts.md`:

```markdown
# [Topic Name] - Fact File

## FINDING-YYYY-MM-DD-N

**Topic:** [Short topic name/category]

**Observation:**
[2-5 sentences describing the finding, observation, or fact captured]

**Source:** [Citation to authoritative source, URL, or "User observation"]

**Date captured:** YYYY-MM-DD

---
```

---

# Template Guidelines

## File Header

Start each fact file with H1 header identifying the topic:

```markdown
# [Topic Name] - Fact File
```

Example: `# GitHub API - Fact File`

## Finding Entry Format

Each finding includes:

- **FINDING-YYYY-MM-DD-N**: Unique identifier (date-based + incrementing sequence per day)
- **Topic:** Short category name for this finding
- **Observation:** 2-5 sentences describing the fact, observation, or claim
- **Source:** Citation to authoritative documentation, URL, or "User observation" for direct knowledge
- **Date captured:** When the finding was captured (YYYY-MM-DD)

Separate findings with horizontal rule (`---`).

---

# Usage in Topic Bootstrap

When the analysis skill's topic bootstrap feature creates a new topic:

**MUST:**
1. Create `[topic-slug]-facts.md` using this template
2. Add file header with topic name
3. Initialize as empty with no findings (ready for first fact capture)
4. Do NOT add any initial findings during bootstrap

**MUST NOT:**
- Add sections beyond those in this template
- Modify the template structure
- Add metadata not specified in the template

---

# Finding Capture Workflow

When capturing findings during research:

1. Append new finding using FINDING-YYYY-MM-DD-N format
2. Increment N for each finding on the same day
3. Include complete Observation section with sufficient detail
4. Always include Source citation
5. Use today's date in Date captured field

See [fact-capture.md](fact-capture.md) for complete fact capture workflow requirements.
