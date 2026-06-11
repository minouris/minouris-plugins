# Analysis Index Maintenance

**This file is loaded when: You need to update or create the analysis index file.**

---

# Embedded Rules

## Literal Specification Compliance (from /src/claude/rules/literal-specification.md)

**Index Structure is Expressly Specified - Compliance is MANDATORY:**

**MUST:**
- Follow the exact index file structure as specified
- Use only the sections and fields in the specification
- Maintain exact heading levels, spacing, and content order
- Preserve the standardized table format for Findings table

**MUST NOT:**
- Add sections or fields beyond specification
- Add metadata or organizational headers not specified
- Enhance index structure with additional context
- Modify the index format "for improvements"

---

## Markdown Formatting Standards (from /.claude/rules/markdown-formatting.md)

### Filename Conventions (MANDATORY)

**MUST:**
- Use lower-snake-case for index filenames (e.g., `topic_index.md`)
- Use `.md` extension for all Markdown files

**MUST NOT:**
- Use kebab-case (e.g., `topic-index.md`)
- Use camelCase (e.g., `topicIndex.md`)
- Use PascalCase (e.g., `TopicIndex.md`)
- Use spaces in filenames

---

## Existing Rules

### Always Update After Changes (MANDATORY)

**MUST:**
- Update index after appending to fact files
- Update index after archiving disproven findings
- Update findings table when findings are added or archived
- Include file paths and last updated timestamps
- Keep index concise and navigable
- Add ALL subtopic findings to the main topic index

**MUST NOT:**
- Skip index updates
- Leave index out of sync with fact files
- Leave findings table out of sync with fact files
- Create separate index files for subtopics

---

## Index File Location

```
.memory/[topic]/[topic]-index.md
```

**Example:**
```
.memory/ai-problems-analysis/ai-problems-analysis-index.md
```

---

## Index Structure (MANDATORY)

```markdown
# [Topic] Index

**Last Updated:** YYYY-MM-DD HH:MM

---

## Fact Files

- [[topic]-facts.md]([topic]-facts.md) - [Brief description of research scope]
  - Last updated: YYYY-MM-DD HH:MM
  - Disproven: [[topic]-facts-disproven.md]([topic]-facts-disproven.md) (N findings)

- [[topic]-[subtopic]-facts.md]([topic]-[subtopic]/[topic]-[subtopic]-facts.md) - [Brief description]
  - Last updated: YYYY-MM-DD HH:MM
  - Disproven: [[topic]-[subtopic]-facts-disproven.md]([topic]-[subtopic]/[topic]-[subtopic]-facts-disproven.md) (N findings)

[... additional fact files ...]

---

---

## Findings

| Finding | Topic | Name |
|---------|-------|------|
| [FINDING-YYYY-MM-DD-1]([topic]-facts.md#finding-yyyy-mm-dd-1) | Topic Name | Finding Name |

---

## Disproven Findings

*No findings have been disproven yet.*
```

---

## When to Update Index

**CRITICAL:** The analysis index findings table is updated ONLY by the verify-analysis skill after verification completes. Do NOT manually update the findings table when appending facts.

Perform these manual index updates:

1. **Appending to fact file**
   - Update "Last updated" timestamp for that fact file (in Fact Files section)
   - **DO NOT update Findings table** - facts are added to Findings table only after verification by verify-analysis

2. **Creating new subtopic file**
   - Add new entry in "Fact Files" section in the main topic index
   - Include brief description of subtopic scope
   - Include "Last updated" timestamp

3. **Archiving disproven finding** (by verify-analysis)
   - Add or update "Disproven:" line with count
   - If it's the first disproven finding, add the line
   - If archive already exists, increment the count
   - Remove finding from Findings table

**Post-Verification Updates (verify-analysis skill):**

After verify-analysis completes verification, the following are updated automatically:
- Findings table: Add verified finding in alphabetically sorted position
- "Last Updated" timestamp of the main index

---

## Knowledge Summary Maintenance

**Every topic index must include a "Knowledge Summary" section** that allows agents to quickly understand what knowledge a topic contains and whether it's relevant to their task.

### Knowledge Summary Structure

Add this section immediately after the topic title, before other sections:

```markdown
## Knowledge Summary

**Overview:** [One paragraph describing what knowledge this topic contains, target audience, and primary use cases]

**Research Domains:** [List 3-5 key domains/areas covered, comma-separated]

**Core Terminology:** [List 5-7 key terms/concepts that define the topic's scope]

**Verification Status:**
- Verified: N findings
- Unverified: N findings
- Disproven: N findings
- **Verification Rate:** N%

**Total Findings:** N

**Subtopics:** [If applicable, list any subtopic areas with finding count in parentheses]

**Last Verified:** YYYY-MM-DD (most recent verification run)
```

### When to Create/Update Knowledge Summary

**Create when:**
- Topic index is first created (before any findings captured)
- Can use placeholder text if topic purpose unclear

**Update when:**
- First 5 verified findings in topic (populate "Verified" count, "Verification Rate")
- Topic scope changes or expands (update "Research Domains", "Subtopics")
- Significant verification milestone reached (10 verified, 50% verified, 100% verified)
- New subtopic created (add to subtopic list)

**MUST:**
- Reflect actual topic contents accurately
- Update finding counts from topic index Findings table
- Include all active subtopics
- Use clear, agent-readable language

---

## Central Knowledge Base Index

The central knowledge base index at `.memory/KNOWLEDGE_BASE.md` provides a single entry point for discovering all research across all topics. This file enables agents to locate relevant knowledge without navigating the directory structure.

### When Central Index is Updated

**By verify-analysis skill:**
- After verification run completes, if this was the first verification for a topic
- When verification rate of topic reaches 100%
- Automatic update of verification counts and "Last Verified" timestamp per topic

**Manual review (end of session):**
- After session with significant new findings added to a topic
- If topic scope expanded (add to "Quick Search Guide" table)
- If Knowledge Summary changed substantially

### Central Index Content to Maintain

**Keep in sync with topic indexes:**
- `Total Findings` count per topic
- `Verification Status` (verified/unverified/disproven counts)
- `Last Updated` and `Last Verified` dates
- Subtopic lists
- Quick Search Guide: Add entry if new research domain discovered

**Minimal updates needed:**
- Topic summaries do not need word-for-word sync; overview paragraph can be refreshed during quarterly reviews
- Quick Search Guide table: Add row if new research domain found; remove if domain no longer relevant

**DO NOT edit:**
- Directory structure or folder organization
- File path links (these are permanent once set)
- Historical maintenance log



If index doesn't exist, create it with this minimal structure:

```markdown
# [Topic] Index

**Last Updated:** YYYY-MM-DD HH:MM

---

## Fact Files

- [[topic]-facts.md]([topic]-facts.md) - [One-sentence description]
  - Last updated: YYYY-MM-DD HH:MM

---

## Findings

| Finding | Topic | Name |
|---------|-------|------|
| [FINDING-YYYY-MM-DD-1]([topic]-facts.md#finding-yyyy-mm-dd-1) | Topic Name | Finding Name |

---

## Disproven Findings

*No findings have been disproven yet.*
```

---

## Listing Subtopic Files

When a topic has multiple subtopic files, list them all:

```markdown
## Fact Files

### Main Topic

- [[topic]-facts.md]([topic]-facts.md) - Overview and cross-cutting findings
  - Last updated: YYYY-MM-DD HH:MM

### Subtopics

- [[topic]-hallucination-facts.md]([topic]-hallucination/[topic]-hallucination-facts.md) - Hallucination and dishonesty problems
  - Last updated: YYYY-MM-DD HH:MM
  - Disproven: [[topic]-hallucination-facts-disproven.md]([topic]-hallucination/[topic]-hallucination-facts-disproven.md) (3 findings)

- [[topic]-overeagerness-facts.md]([topic]-overeagerness/[topic]-overeagerness-facts.md) - Overeagerness and proactivity issues
  - Last updated: YYYY-MM-DD HH:MM
```

---

## Disproven Count

When adding disproven companion file reference:

**First disproven finding (create line):**
```markdown
- Disproven: [.memory/[topic]-facts-disproven.md](.memory/[topic]-facts-disproven.md) (1 finding)
```

**Additional disproven findings (update count):**
```markdown
- Disproven: [.memory/[topic]-facts-disproven.md](.memory/[topic]-facts-disproven.md) (5 findings)
```

**No disproven findings (omit line entirely):**
```markdown
- [.memory/[topic]-facts.md](.memory/[topic]-facts.md) - [Description]
  - Last updated: YYYY-MM-DD HH:MM
```

---

## Findings Table (MANDATORY)

List all findings from the topic and all subtopics in a table format, sorted alphabetically by finding name.

**MUST:**
- Include three columns: Finding (ID as link), Name (title), Topic (category)
- Link Finding column to the actual finding heading using anchor syntax
- Sort findings alphabetically by Name column
- When names are identical, sort by Topic column (alphabetically)
- Update table when appending findings
- Update table when archiving findings (remove archived findings)

**MUST NOT:**
- Omit findings table from index
- Include findings without all three columns
- List findings in unsorted order
- Include archived findings in the table

**Table Format:**
```markdown
## Findings

| Finding | Name | Topic |
|---------|------|-------|
| [FINDING-2026-03-04-12](#finding-2026-03-04-12) | API Authentication Methods | Authentication |
| [FINDING-2026-03-04-15](#finding-2026-03-04-15) | CLAUDE.md Locations and Scope | Configuration |
| [FINDING-2026-03-04-8](#finding-2026-03-04-8) | Hook Event Types | Automation |
```

**Sorting rules:**
1. Sort primarily by Name (alphabetical, case-insensitive)
2. If names match, sort by Topic (alphabetical comparison)
3. Finding ID is for reference only, not used for sorting

**When updating findings table:**

1. **New finding added:** Add row in alphabetically correct position by name
2. **Finding archived:** Remove row from table

---

## Analysis Outputs Section

Track generated analysis documents:

```markdown
## Analysis Outputs

- [`ai-programming-problems-analysis.md`](ai-programming-problems-analysis.md) - Comprehensive analysis of AI coding assistant problems
  - Generated: 2026-02-24 HH:MM
  - Sources: ai-problems-analysis-facts.md, ai-problems-analysis-hallucination-facts.md, ai-problems-analysis-overeagerness-facts.md

- [`authentication-implementation-guide.md`](authentication-implementation-guide.md) - Procedure for implementing OAuth authentication
  - Generated: 2026-02-23 HH:MM
  - Sources: auth-implementation-facts.md
```

---

## Index Update Workflow

1. **Read current index** (if it exists)

2. **Determine what changed:**
   - New fact file entry added?
   - Fact file timestamp updated?
   - New finding added?
   - Finding archived?
   - Disproven count changed?
   - New analysis output created?

3. **Update index** using Edit tool:
   - Modify only the relevant sections
   - Update Findings table (add/remove rows, maintain alphabetical sort)
   - Update "Last Updated" timestamp at top
   - Keep existing structure intact

4. **If index doesn't exist**, create it using Write tool with initial structure

---

## Example Complete Index

```markdown
# AI Problems Analysis Index

**Last Updated:** 2026-02-24 15:30

---

## Fact Files

### Main Topic

- [.memory/ai-problems-analysis-facts.md](.memory/ai-problems-analysis-facts.md) - Overview and cross-cutting research
  - Last updated: 2026-02-24 15:30

### Subtopics

- [.memory/ai-problems-analysis-hallucination-facts.md](.memory/ai-problems-analysis-hallucination-facts.md) - Hallucination and dishonesty problems
  - Last updated: 2026-02-24 14:20
  - Disproven: [.memory/ai-problems-analysis-hallucination-facts-disproven.md](.memory/ai-problems-analysis-hallucination-facts-disproven.md) (2 findings)

- [.memory/ai-problems-analysis-overeagerness-facts.md](.memory/ai-problems-analysis-overeagerness-facts.md) - Overeagerness and proactivity issues
  - Last updated: 2026-02-24 12:45

- [.memory/ai-problems-analysis-amnesia-facts.md](.memory/ai-problems-analysis-amnesia-facts.md) - Context window and memory issues
  - Last updated: 2026-02-23 16:10
  - Disproven: [.memory/ai-problems-analysis-amnesia-facts-disproven.md](.memory/ai-problems-analysis-amnesia-facts-disproven.md) (1 finding)

---

## Findings

| Finding | Name | Topic |
|---------|------|-------|
| [FINDING-2026-02-24-3](#finding-2026-02-24-3) | Attention Mechanism Limitations | Context |
| [FINDING-2026-02-24-7](#finding-2026-02-24-7) | Behavioral Training Artifacts | Training |
| [FINDING-2026-02-24-1](#finding-2026-02-24-1) | Confidence Calibration Issues | Hallucination |
| [FINDING-2026-02-23-5](#finding-2026-02-23-5) | Context Window Management | Memory |
| [FINDING-2026-02-24-9](#finding-2026-02-24-9) | False Positive Patterns | Accuracy |

---

## Analysis Outputs

- [`ai-programming-problems-analysis.md`](ai-programming-problems-analysis.md) - Comprehensive analysis of AI coding assistant problems
  - Generated: 2026-02-24 15:45
  - Sources: ai-problems-analysis-facts.md, ai-problems-analysis-hallucination-facts.md, ai-problems-analysis-overeagerness-facts.md, ai-problems-analysis-amnesia-facts.md
```
