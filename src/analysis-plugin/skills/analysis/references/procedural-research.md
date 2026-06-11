# Procedural Research Workflow

**This file is loaded when: You need to find, test, and verify a procedure or process.**

---

# Embedded Rules

## Documentation-First Response Requirements (from /src/claude/rules/documentation-first.md)

### Two-Stage Text Search (MANDATORY)

When searching for procedures within documentation, use a two-stage approach before concluding that a procedure is unavailable.

**Stage 1 — Keyword search:**
- Use Grep or search tools as the initial approach
- Try multiple related terms, synonyms, and variations
- Search for procedure names, command names, configuration options

**If Stage 1 yields no results or only false positives, proceed to Stage 2:**

**Stage 2 — Direct file examination:**
- Read the full relevant documentation files directly using Read tool
- Procedures, configuration guidelines, and step-by-step instructions are frequently expressed in natural language
- Do NOT report a procedure as unavailable until Stage 2 has been completed

**MUST NOT:**
- Report that procedure cannot be found after only a keyword search
- Treat search/grep returning zero results as confirmation that procedure does not exist

---

## Existing Rules

### Documentation-First (MANDATORY)

**MUST:**
- Search for and reference official documentation sources
- Verify information against authoritative sources before recording
- Use two-stage text search: keyword search → direct file examination
- Read documentation directly from files, not from cached context

**MUST NOT:**
- Rely solely on general knowledge or training data
- Report information unavailable after only keyword search
- Use cached documentation content without re-reading

---

# Separation of Concerns

## Your Responsibilities

When you execute procedural-research, you are responsible ONLY for:
- Clarifying the procedure being researched and target environment
- Conducting two-stage text searches through documentation
- Testing procedures when possible
- Collecting findings, test results, and observations
- **Invoking the fact-capture flow** to record all findings

## What Fact-Capture Does

**DO NOT** attempt fact-capture implementation:
- DO NOT format findings entries
- DO NOT manage fact file structure
- DO NOT handle verification tags or timestamps
- DO NOT update indices
- DO NOT extract or verify terms
- DO NOT archive disproven findings

You MUST delegate all fact recording, verification, and maintenance to the fact-capture flow.

---

## When to Use This Workflow

- Finding installation procedures
- Testing configuration steps
- Verifying deployment processes
- Documenting command sequences
- Any task requiring step-by-step verification

---

## Workflow Steps

1. **Clarify scope**: Ask what procedure is being researched and what the target context/environment is

2. **Confirm topic slug**: Confirm the topic slug with the user (e.g., `pterodactyl-install`); this is used for file naming and operation logging throughout this work

3. **Search documentation**: Search web/docs using WebFetch/WebSearch for procedures

4. **Capture findings**: For each finding or observation, invoke the fact-capture flow:

   **Fact-Capture Flow Invocation:**
   ```
   Invoke fact-capture flow with:
   - topic: [topic-slug]
   - observation: [finding description - procedure step, requirement, variation, test result, workaround, etc.]
   - source: [citation to authoritative documentation or testing observation]
   - subtopic: [optional: if finding belongs to a specific subtopic category]
   - clarifies: [optional: FINDING-YYYY-MM-DD-N if this clarifies an existing finding]
   ```

   **When you invoke fact-capture for a finding:**

   Fact-capture performs:
   - Generating FINDING-YYYY-MM-DD-N identifiers
   - Creating/appending to fact files with proper structure
   - Adding Captured timestamps (YYYY-MM-DD HH:MM)
   - Adding Verified tags [NOT YET VERIFIED - requires verification workflow]
   - Managing file locations and folder organisation
   - Maintaining the main topic index
   - Handling subtopic creation when thresholds are exceeded

5. **Test if possible**: If testing is possible, document all attempts and outcomes:
   - Exact commands executed
   - Output and errors
   - Environment details (OS, versions, configuration)
   - Success/failure clearly indicated
   - Workarounds discovered
   - Dead ends and reasons they failed

   For each test result, invoke the fact-capture flow to record the finding.

6. **Iterate**: Continue capturing findings from testing results without pausing for approval. Fact-capture handles all recording, verification, and maintenance.

7. **Handle disproven findings**: When user disproves a finding, invoke the fact-capture flow with:
   ```
   Invoke fact-capture flow with:
   - action: archive-disproven
   - finding-id: FINDING-YYYY-MM-DD-N
   - reason: [user explanation of why finding is disproven]
   ```

   **When you invoke fact-capture to archive a disproven finding:**

   Fact-capture performs:
   - Moving the finding to the `-disproven.md` archive
   - Recording the disproof metadata
   - Updating the index

---

# Fact Capture Interface

See [fact-capture.md](fact-capture.md) for:
- Complete flow invocation specification
- Idempotence guarantees
- File structure contracts
- Verification workflow integration
- Term extraction and linking requirements

**CRITICAL:** Do not read fact-capture.md as a guideline. It defines the fact-capture flow contract. Research workflows invoke this flow; they do not implement it.

---

# Clarifying Existing Facts

When new information (from testing or further research) affects or refines an existing fact, invoke the fact-capture flow with the `clarifies` parameter:

```
Invoke fact-capture flow with:
- topic: [topic-slug]
- observation: [clarifying or refining information]
- source: [source of clarification - documentation or testing observation]
- clarifies: FINDING-2026-02-24-3  (the finding being clarified)
```

Fact-capture appends the clarification as a new finding with proper linking, storing it with reference to the original.

---

# Iterative Refinement

Continue iterating on procedures by invoking the fact-capture flow:
- Append findings for variations and workarounds
- Reference previous findings when building on them
- Note which variations work in which environments
- Document dead ends and reasons they failed

**MUST NOT:**
- Attempt to edit existing findings (invoke fact-capture with `clarifies` instead)
- Delete failed attempts (they are recorded by the fact-capture flow)
- Skip documenting workarounds or failed approaches

