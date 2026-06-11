# Update Analysis Index

**This file is loaded when: You need to update the analysis index to reflect a newly verified finding.**

---

# Embedded Rules

## Literal Specification Compliance (from /src/claude/rules/literal-specification.md)

**Index Update Format is Expressly Specified - Compliance is MANDATORY:**

**MUST:**
- Follow the exact index update format as specified for each operation
- Use only the sections and fields in the specification
- Maintain exact table structure and heading levels
- Preserve the Findings table format character-for-character

**MUST NOT:**
- Add fields to the Findings table beyond specification
- Add metadata or summary sections not specified
- Modify the index structure "for improvements"
- Change the sorting order or table format

---

## Markdown Formatting Standards (from /.claude/rules/markdown-formatting.md)

### Filename Conventions (MANDATORY)

**MUST:**
- Use lower-snake-case for index filenames (e.g., `topic_index.md`)
- Use `.md` extension for all Markdown files

**MUST NOT:**
- Use kebab-case (e.g., `topic-index.md`)
- Use camelCase (e.g., `topicIndex.md`)
- Use spaces in filenames

---

## Execution

After verification is complete, update the analysis index to include the newly verified finding. This maintains a complete and current index of all active findings in the topic.

---

## Index File Location

```
.memory/[topic]/[topic]-index.md
```

Example:
```
.memory/github-api/github-api-index.md
```

---

## Index Update Operations

### 1. Add or Update "Last Updated" Timestamp

Update the timestamp at the top of the index:

```markdown
# [Topic] Index

**Last Updated:** YYYY-MM-DD HH:MM
```

### 2. Update Fact Files Section

If this is the first verified finding in this file, add entry to the "Fact Files" section:

```markdown
## Fact Files

- [[topic]-facts.md]([topic]-facts.md) - [Brief description]
  - Last updated: YYYY-MM-DD HH:MM
```

### 3. Add to Findings Table

Add finding to the Findings table in alphabetically sorted position (by Topic, then Name), including any relevant terms:

```markdown
## Findings

| Finding | Topic | Name | Terms |
|---------|-------|------|-------|
| [FINDING-YYYY-MM-DD-N](#finding-yyyy-mm-dd-n) | Topic Name | Finding Name | [term1](#term1), [term2](#term2) |
```

---

## Requirements

**MUST:**
- Update "Last Updated" timestamp
- Add finding to Findings table in correct alphabetical position
- Use correct finding anchor format (lowercase, hyphens)
- Preserve existing structure and formatting

**MUST NOT:**
- Leave index out of sync with active findings
- Break existing links or references
- Remove archived findings from the index
- Update file directly in memory without using Edit tool

---

## Integration with Term Verification

For term verifications using the same topic, also update the term-related index entries if applicable (see term-indexing.md). However, maintain separate fact findings and term indices.

---

## Sorting Rules

**Findings table:**
- Primary sort: Topic (alphabetical, case-insensitive)
- Secondary sort: Name (alphabetical, case-insensitive)
- Finding ID is for reference only, not used for sorting
- Terms column is optional and can accumulate as terms are extracted and verified

---

## Output

The analysis index is now updated to reflect the newly verified finding and remains current and navigable.
