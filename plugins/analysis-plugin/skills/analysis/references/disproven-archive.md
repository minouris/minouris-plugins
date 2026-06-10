# Disproven Findings Archive

**This file is loaded when: You need to archive a disproven finding.**

---

# Embedded Rules

## Literal Specification Compliance (from /src/claude/rules/literal-specification.md)

**Archive Entry Format is Expressly Specified - Compliance is MANDATORY:**

**MUST:**
- Follow the disproven finding archive format exactly as specified
- Include all required fields: original finding, reason for disproof, evidence, date archived
- Preserve exact structure (heading levels, spacing, field order)
- Use the specified template without additions

**MUST NOT:**
- Add fields to archive entries beyond specification
- Add explanatory sections or metadata not specified
- Modify the archive format for convenience
- Add interpretations or additional context not in the specification

---

## Existing Rules

### Never Delete (MANDATORY)

**MUST:**
- Move disproven findings to `-disproven.md` companion file
- Add disproof metadata (date disproven, contradicting evidence, reason)
- Remove from main fact file completely
- Preserve history for transparency

**MUST NOT:**
- Delete disproven findings
- Leave disproven findings in the main fact file
- Skip recording the reason for disproof

---

## When to Archive

Archive a finding when:
- User explicitly disproves it
- New evidence contradicts it
- Further research reveals it's inaccurate
- Source is found to be unreliable

---

## Archive File Naming

**For main topic file:**
```
.memory/[topic]-facts.md → .memory/[topic]-facts-disproven.md
```

**For subtopic files:**
```
.memory/[topic]-[subtopic]-facts.md → .memory/[topic]-[subtopic]-facts-disproven.md
```

---

## Disproven Entry Format (MANDATORY)

```markdown
### FINDING-YYYY-MM-DD-N (DISPROVEN)
**Originally Captured:** YYYY-MM-DD HH:MM
**Disproven:** YYYY-MM-DD HH:MM
**Original Source:** [original source]
**Contradicting Evidence:** [what disproved this]

~~[Original finding description]~~

**Reason for Disproof:** [Why this is no longer considered accurate]
```

**Example:**
```markdown
### FINDING-2026-02-23-7 (DISPROVEN)
**Originally Captured:** 2026-02-23 14:20
**Disproven:** 2026-02-24 10:15
**Original Source:** https://docs.example.com/old-api
**Contradicting Evidence:** User confirmed API endpoint changed in v2

~~The API uses `/api/users` endpoint for user management.~~

**Reason for Disproof:** Endpoint was changed to `/api/v2/users` in API v2 release (Jan 2026). The original documentation was for deprecated v1 API.
```

---

## Archive Workflow

1. **Identify disproven finding** in main fact file (e.g., `.memory/[topic]-facts.md`)

2. **Copy finding** to archive file (`.memory/[topic]-facts-disproven.md`):
   - Create archive file if it doesn't exist
   - Add DISPROVEN metadata
   - Strikethrough original content
   - Add reason for disproof

3. **Remove from main fact file** using Edit tool:
   - Remove the entire FINDING block
   - Do NOT leave any trace in main file

4. **Update index** to note disproven companion file exists:
   ```markdown
   - Disproven: [.memory/[topic]-facts-disproven.md](.memory/[topic]-facts-disproven.md) (N findings)
   ```

---

## Archive File Structure

If the archive file doesn't exist, create it with this structure:

```markdown
# [Topic] Facts - Disproven

**Purpose:** This file contains findings from `.memory/[topic]-facts.md` that were found to be inaccurate, outdated, or contradicted by evidence.

**Archive Date:** YYYY-MM-DD
**Source File:** `.memory/[topic]-facts.md`

Findings are preserved here for transparency and to document the research process, including dead ends and corrected information.

---

[Disproven findings in chronological order]
```

---

## Why Archive Rather Than Delete

**Transparency:**
- Shows what was investigated
- Documents dead ends
- Preserves research history

**Traceability:**
- Others can see what was initially believed
- Explains why certain paths were explored
- Shows evidence used to disprove

**Learning:**
- Prevents re-investigating disproven theories
- Documents what sources were unreliable
- Helps refine research methodology

---

## Handling Clarifications vs. Disproof

**Clarification** (append to fact file):
- Original finding is partially correct
- New information refines or extends it
- Core claim remains valid

**Disproof** (archive to disproven file):
- Original finding is fundamentally incorrect
- New evidence contradicts it
- Core claim is invalid

**Example of clarification (do NOT archive):**
```markdown
### FINDING-2026-02-24-10
**Clarifies:** FINDING-2026-02-24-3

API v2 endpoint uses `/api/v2/users` not `/api/users`, but v1 is still supported until 2027.
```

**Example of disproof (DO archive):**
```markdown
### FINDING-2026-02-24-11 (DISPROVEN)
**Contradicting Evidence:** User testing showed feature doesn't exist in any version

~~The API supports bulk user deletion via DELETE /api/users/bulk endpoint.~~

**Reason for Disproof:** Testing confirmed no bulk deletion endpoint exists. Feature request is open but not implemented.
```
