# Archive Disproven Finding

**This file is loaded when: You need to archive a finding that has been verified as DISPROVEN.**

---

# Embedded Rules

## Literal Specification Compliance (from /src/claude/rules/literal-specification.md)

**Disproven Finding Archive Format is Expressly Specified - Compliance is MANDATORY:**

**MUST:**
- Follow the disproven finding archive format exactly as specified
- Include all required fields: original finding (verbatim), reason for disproof, contradicting evidence (verbatim), verification working document link
- Preserve exact structure (heading levels, spacing, field order)
- Use the specified template without additions

**MUST NOT:**
- Add fields to archive entries beyond specification
- Add explanatory sections or metadata not specified
- Modify the archive format for convenience
- Add interpretations or reasoning beyond what specification requires

---

## Execution

Move disproven findings to an archive file separate from the active fact file to maintain a clean active record while preserving full history of all findings including those later found to be inaccurate.

---

## Archive File Location

Create in the same directory as the original fact file:

```
.memory/[topic]/[topic]-facts-disproven.md
```

For subtopics:

```
.memory/[topic]/[topic]-[subtopic]/[topic]-[subtopic]-facts-disproven.md
```

---

## Archive Structure

Create or append to `-disproven.md` file:

```markdown
# [Topic] Disproven Findings

**Archive of findings that failed verification or were found to be inaccurate.**

---

### FINDING-YYYY-MM-DD-N: [Finding Title]

**Original Finding:**
```
[Original finding text from active file]
```

**Archived:** YYYY-MM-DD
**Verification Date:** YYYY-MM-DD
**Reason:** [Specific reason why finding was disproven]

**Evidence:**
> [Verbatim quote from source contradicting the finding]

Source: [source-url]

**Verification Details:** See [verification working document]({path}#{anchor})

---
```

---

## Requirements

**MUST:**
- Include original finding text verbatim
- Include specific reason why finding was disproven
- Include contradicting evidence from authoritative source
- Include link to verification working document
- Archive to `-disproven.md` file, NOT delete
- Preserve complete audit trail
- Maintain timestamp showing when finding was archived

**MUST NOT:**
- Delete findings without archiving
- Summarize or paraphrase the finding (use verbatim)
- Omit contradicting evidence
- Leave audit trail incomplete
- Mix disproven findings with active findings

---

## Processing Flow

1. **If archive file doesn't exist**: Create new with header section
2. **If archive file exists**: Append new archived finding section
3. **Link to verification**: Include reference to verification working document
4. **Remove from active file**: Finding will be removed when fact file is finalized

---

## Output

The disproven finding is now preserved in archive for audit purposes and will be removed from the active fact file during finalization.
