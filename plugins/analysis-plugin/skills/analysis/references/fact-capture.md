# Fact-Capture Flow Specification

**When you implement the fact-capture flow, use this specification to understand your responsibilities.**

---

# Your Responsibilities (What You MUST Do)

When you are invoked to capture a finding, you are **solely responsible** for:

## Finding Recording

**MUST:**
- Generate unique FINDING-YYYY-MM-DD-N identifiers
- Create or append to fact files in proper location (`.memory/[topic]/[topic]-facts.md` or `.memory/[topic]/[topic]-[subtopic]/[topic]-[subtopic]-facts.md`)
- Add **Captured:** YYYY-MM-DD HH:MM timestamp to each finding
- Add **Verified:** [NOT YET VERIFIED - requires verification workflow] tag to each new finding
- Record complete observation text with source citation

## File Structure Management

**MUST:**
- Create topic directories (`.memory/[topic]/`) when needed
- Create subtopic directories (`.memory/[topic]/[topic]-[subtopic]/`) when thresholds are exceeded
- Manage file naming conventions and folder organisation
- Maintain folder-based structure (.memory/[topic]/ not flat .memory/ root)
- Enforce maximum file size (40,000 characters) with automatic subtopic creation when exceeded

## Index Maintenance

**MUST:**
- Maintain `.memory/[topic]/[topic]-index.md` as single source of truth for all findings
- Add findings to findings table only after capturing in fact file
- Organise findings table by Topic (primary) and Name (secondary)
- Link findings to their actual location in fact files

**MUST NOT:**
- Create per-subtopic indices; all findings route through main topic index

## Clarification Handling

**MUST:**
- Append clarifications as new FINDING-YYYY-MM-DD-N entries
- Link clarifications to original findings via `Clarifies:` reference
- Leave original findings unchanged
- Store clarifications in same fact file as originals

## Documentation-First Compliance

**MUST:**
- Enforce that all findings reference authoritative sources
- Reject findings without proper source citations

## Verification Invocation

**MUST:**
- Invoke verify-analysis subagent immediately after recording the finding
- Invoke synchronously in isolated context (do not return to research workflow until verification completes)
- Pass finding-id and topic to verify-analysis subagent
- Wait for verification to complete before proceeding
- Return verification status in response to research workflow:
  - If verified: Return status "captured" with VERIFIED metadata and source URL
  - If disproven: Accept disproven archive from verify-analysis; return status "rejected"
  - If unverifiable: Return status "captured" with [NOT YET VERIFIED] tag

**Verification is a mandatory blocking operation.** Do not return to the research workflow with a finding that has not been submitted to verify-analysis for verification.

---

# Invocation Contract

## Single Finding Per Invocation

Fact-capture is designed as a **single-concern, single-fact operation**:

- **One invocation = one finding recorded**
- Fact-capture accepts a single finding observation and records it
- Fact-capture returns immediately after recording (or when duplicate detected)
- No batch operations; research workflows invoke once per finding

## Return Value

Fact-capture MUST return status to the invoking research workflow:

```
Return:
- status: "captured" | "rejected" | "duplicate"
- finding-id: FINDING-YYYY-MM-DD-N (if captured or duplicate)
- reason: [explanation if rejected or duplicate]
- verification-status: [NOT YET VERIFIED | VERIFIED on YYYY-MM-DD by source-url | REJECTED on YYYY-MM-DD by reason]
```

**Status meanings:**
- `captured`: Finding was successfully recorded, verified synchronously
- `duplicate`: Finding already exists; same FINDING-YYYY-MM-DD-N returned with existing verification status
- `rejected`: Finding was rejected (missing source citation, or disproven during verification); not recorded

---

# Downstream Operations (You Invoke These)

**You are responsible for invoking verification via subagents, maintaining independent agent context for isolation:**

## Synchronous Verification Invocation

After recording a finding, invoke verify-analysis subagent (synchronously, in isolated context):

```
Invoke verify-analysis subagent with:
- action: "verify-fact"
- finding-id: FINDING-YYYY-MM-DD-N
- topic: [topic-slug]
```

**When verify-analysis completes:**
- If verified: Return with verification status VERIFIED and source URL
- If disproven: verify-analysis archives to `-disproven.md`; you return rejection status
- If unverifiable: Return with [NOT YET VERIFIED] tag

**verify-analysis responsibilities (in independent context):**
- Verify finding content against authoritative sources
- Archive findings to `-disproven.md` if false
- Update finding tags with verification metadata
- Report results to you

---

# Your Guarantees (Idempotence)

**You MUST be idempotent and absolute:**

1. **Multiple invocations of the same finding are safe**: When invoked twice with identical parameters, record the finding once (do not duplicate)

2. **Finding references are globally consistent**: When invoked with a reference to another finding by ID (e.g., `clarifies: FINDING-2026-04-04-01`), work consistently regardless of invocation order

3. **Fact files remain in valid state**: Do NOT leave fact files in incomplete or inconsistent states

4. **Index always reflects actual findings**: Update index synchronously with fact capture; never let index and fact files diverge

5. **File location migrations are transparent**: When a finding is moved to a new subtopic file due to size thresholds, keep the finding reference (e.g., `FINDING-2026-04-04-01`) valid and consistent

---

# Research Workflow Restrictions

Research workflows (procedural-research, analytical-research) **MUST NOT**:

- Write directly to fact files
- Manage file structure or folder organisation
- Update indices manually
- Format fact entries
- Create finding identifiers
- Add verification tags
- Handle file size management
- Create or manage subtopics
- Extract or link terms
- Archive disproven findings
- Verify facts or terms

Research workflows **MUST** invoke you for all recording and maintenance tasks. Verification depends on downstream flows (verify-analysis, term-capture).

---

# Implementation Details

**CRITICAL:** This specification defines what YOU MUST DO (not HOW you implement it).

Implementation details (which tools you use, file I/O patterns, parsing logic, etc.) are encapsulated within you and **MUST NOT be visible to research workflows**.

Research workflows invoke you by name with defined parameters. You are a black box to them.

---

# Flow Idempotence Examples

**Example 1: Duplicate invocation**
```
First invocation:
- topic: github-api
- observation: "REST API returns 200 on success"
- source: https://docs.github.com/en/rest

Second invocation with identical parameters:
- Result: Finding not duplicated; same FINDING-YYYY-MM-DD-N used
```

**Example 2: Clarification ordering**
```
Research captures: FINDING-2026-04-04-01 (initial observation)
Research captures: FINDING-2026-04-04-02 (clarifies FINDING-2026-04-04-01)
Research captures: FINDING-2026-04-04-03 (clarifies FINDING-2026-04-04-01)

Result: All clarifications properly linked and ordered, links remain valid regardless of invocation sequence
```

**Example 3: Downstream invocation**
```
Fact-capture records: FINDING-2026-04-04-01
→ Fact-capture invokes term-capture flow for concept extraction
→ Term-capture creates TERM-[topic]-YYYY-MM-DD-N
→ Fact-capture invokes verify-analysis for term verification
→ verify-analysis updates term with verification status
→ Finding remains unchanged; all updates flow through downstream operations
```

---
