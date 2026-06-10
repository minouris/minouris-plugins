# Operation Logging

**This file is loaded when: You need to log significant operations or initialize a session from operation history.**

---

# Embedded Rules

## Literal Specification Compliance (from /src/claude/rules/literal-specification.md)

**Operation Log Format is Expressly Specified - Compliance is MANDATORY:**

**MUST:**
- Follow the log entry format exactly as specified
- Include all required fields: date, operation type, files modified, summary
- Preserve exact field order and structure
- Use the specified timestamp format

**MUST NOT:**
- Add fields to log entries beyond specification
- Add metadata or summary sections not specified
- Modify the log format for convenience
- Change field names or structure

---

## Existing Rules

### Log After Each Significant Operation (MANDATORY)

**MUST:**
- Run [record-operation](../../../src/claude/prompts/record-operation.prompt.md) with `topic=[slug]` after each significant operation (if the prompt is available in the workspace)
- Record only what changed in the current operation — not a summary of the whole session
- Append to `.memory/[topic]/[topic]-log.md`; never overwrite earlier entries

**MUST NOT:**
- Skip logging because an operation seemed minor
- Log speculative or unconfirmed information
- Overwrite existing log entries

**Note:** The record-operation prompt may not be available in all workspaces. If it's not present, skip this step.

---

## Significant Operations

Log after each of these operations:

1. **Appending findings to a fact file**
   - Which fact file was updated
   - How many findings were added
   - Brief topics covered

2. **Archiving disproven findings**
   - Which findings were moved to disproven file
   - Why they were disproven

3. **Updating the analysis index**
   - What changed in the index
   - New files added or timestamps updated

---

## Log File Location

```
.memory/[topic]/[topic]-log.md
```

**Example:**
```
.memory/ai-problems-analysis/ai-problems-analysis-log.md
```

---

## Log Entry Format

```markdown
## LOG-YYYY-MM-DD-N: [Brief operation description]

**Date:** YYYY-MM-DD HH:MM
**Operation:** [append-findings | archive-disproven | update-index]
**Files Changed:** [list of files]

[Description of what changed in this operation]

**Next Step:** [What should happen next, if relevant]
```

**Example:**
```markdown
## LOG-2026-02-24-3: Appended 5 hallucination findings

**Date:** 2026-02-24 14:30
**Operation:** append-findings
**Files Changed:** .memory/ai-problems-analysis-hallucination-facts.md, .memory/ai-problems-analysis-index.md

Added 5 new findings on documentation-first policy evolution:
- FINDING-2026-02-24-10: Initial symptom-based approach
- FINDING-2026-02-24-11: Shift to training override
- FINDING-2026-02-24-12: Counter: declarations
- FINDING-2026-02-24-13: 8-revision evolution
- FINDING-2026-02-24-14: Compliance gates

Updated index with new timestamp for hallucination facts file.

**Next Step:** Continue research into overeagerness solutions.
```

---

## Session Initialization Protocol (MANDATORY)

When you are invoked in a new session, before anything else:

**Step 1: Ask for topic slug**

Ask: "What topic are we working on? (This sets the session context — e.g., `ai-problems-analysis`)"

**Step 2: Attempt to read operation log**

Once the user provides the topic slug, attempt to read `.memory/[topic]/[topic]-log.md`.

**Step 3: Summarise last operations (if log exists)**

If the log exists, summarise the last 1–3 entries to the user:
- Operation type
- Files changed
- Next step recorded

**Example:**
```
Session context loaded from `.memory/ai-problems-analysis-log.md`.

Last operations:
- LOG-2026-02-24-3 (14:30): Appended 5 hallucination findings. Next step: Continue research into overeagerness solutions.
- LOG-2026-02-24-2 (12:15): Updated analysis index with new subtopic file.
- LOG-2026-02-24-1 (10:45): Created subtopic file for overeagerness research.

Ready to continue.
```

**Step 4: Confirm readiness**

Confirm: "Session context loaded from `.memory/[topic]/[topic]-log.md`. Ready to continue."

**Step 5: If no log exists**

If no log exists, confirm: "No previous log found for `[topic]`. Starting fresh."

**MUST NOT:**
- Begin any research or respond to the first task before completing steps 1–5
- Assume a topic slug without asking

---

## Log Workflow

1. **After significant operation**, invoke [record-operation](../../../src/claude/prompts/record-operation.prompt.md) with:
   ```
   topic=[slug] operation=[type] files=[list] description=[what changed]
   ```

2. **Prompt appends to log file**:
   - Reads current log to get next sequence number
   - Appends new LOG entry
   - Includes "Next Step" if relevant

3. **Continue with next operation**

---

## When record-operation Prompt Not Available

If the [record-operation](../../../src/claude/prompts/record-operation.prompt.md) prompt is not available in the workspace:

**MUST:**
- Skip operation logging
- Continue with research workflow
- Note in summary that logging was skipped

**Example:**
```
Operation logging skipped (record-operation prompt not available in this workspace).
```

---

## Log File Structure

If creating log file for first time:

```markdown
# [Topic] Operation Log

**Topic Slug:** [topic]
**Started:** YYYY-MM-DD HH:MM

This log tracks significant research operations for the [topic] analysis, enabling session continuity and progress tracking.

---

[Log entries in chronological order]
```

---

## Benefits of Operation Logging

**Session continuity:**
- Resume research after interruptions
- Restore context in new sessions
- Track progress across multiple sessions

**Transparency:**
- Shows what operations were performed
- Documents decision points
- Provides audit trail

**Collaboration:**
- Other researchers can see what was done
- Next steps are documented
- Handoffs are smooth
