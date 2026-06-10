# Analytical Research Workflow

**This file is loaded when: You need to examine artifacts systematically and capture research findings.**

---

# Embedded Rules

## Two-Stage Text Search (MANDATORY)

When searching for information within artifacts and documentation, use a two-stage approach before concluding that information is unavailable.

**Stage 1 — Keyword search:**
- Use Grep or search tools as the initial approach
- Try multiple related terms, synonyms, and variations
- Search for feature names, configuration keys, code patterns

**If Stage 1 yields no results or only false positives, proceed to Stage 2:**

**Stage 2 — Direct file examination:**
- Read the full relevant files or sections directly using Read tool
- Design rationales, configuration logic, and architectural decisions are frequently expressed in natural language comments
- Do NOT report that information cannot be found until Stage 2 has been completed

**MUST NOT:**
- Report information as unavailable after only a keyword search
- Treat search/grep returning zero results as confirmation that information does not exist
- Skip file examination when keyword search yields no results

---

## Documentation-First (MANDATORY)

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

When you execute analytical-research, you are responsible ONLY for:
- Clarifying research scope and objectives
- Conducting systematic examination of artifacts
- Performing two-stage text searches
- Collecting raw findings and observations
- **Invoking the fact-capture flow** to record findings

## What Fact-Capture Does

**Do NOT** attempt fact-capture implementation:
- DO NOT format findings entries
- DO NOT manage fact file structure
- DO NOT handle verification tags or timestamps
- DO NOT update indices
- DO NOT extract or verify terms
- DO NOT archive disproven findings

You MUST delegate all fact recording, verification, and maintenance to the fact-capture flow.

---

# When to Use This Workflow

- Examining codebase systematically
- Analysing project artifacts (commits, issues, documentation)
- Capturing research findings with proper citation
- Building structured knowledge from artifacts
- Any task requiring systematic investigation and discovery

---

# Workflow Steps

1. **Clarify scope**: Ask which projects/domains to examine and what to look for

2. **Confirm topic slug**: Confirm the topic slug with the user (e.g., `ai-problems-analysis`); this is used for file naming and operation logging throughout this work

3. **Index artifacts**: Create an index of all relevant artifacts (commits, issues, code, documentation)

4. **Systematic examination**: Examine each artifact using Read, Grep, Glob tools

5. **Capture findings**: For each finding or observation, invoke the fact-capture flow:

   **Fact-Capture Flow Invocation:**
   ```
   Invoke fact-capture flow with:
   - topic: [topic-slug]
   - observation: [finding description - fact, observation, theory, hypothesis, dead end, or note]
   - source: [citation to authoritative source, URL, file path, or "User observation"]
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

6. **Continue research**: Keep capturing findings without pausing for approval. The fact-capture flow handles all recording, verification, and maintenance.

7. **Handle disproven findings**: When user disproves a finding during review, invoke the fact-capture flow with:
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

When new information affects or refines an existing fact, invoke the fact-capture flow with the `clarifies` parameter:

```
Invoke fact-capture flow with:
- topic: [topic-slug]
- observation: [clarifying information]
- source: [source of clarification]
- clarifies: FINDING-2026-02-24-3  (the finding being clarified)
```

Fact-capture appends the clarification as a new finding with proper linking.

---
