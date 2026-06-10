# Fact Verification Workflow

**This file is loaded when: You need detailed guidance on verifying individual research findings against authoritative sources.**

---

# Embedded Rules

## Documentation-First Response Requirements (from /src/claude/rules/documentation-first.md)

**Fact verification IS pure documentation-first operation. You must consult authoritative sources to verify every claim in a finding.**

### 1. Documentation Consultation (MANDATORY)

**MUST:**
- Search for and reference official documentation sources for every claim in the finding
- Verify each fact claim against authoritative sources
- Prioritize official documentation over general knowledge

**MUST NOT:**
- Rely on general knowledge or training data to verify facts
- Provide verification without consulting official sources
- Skip documentation research assuming a fact is obviously correct

---

### 2. No Assumptions or Speculation (MANDATORY)

**MUST:**
- Explicitly state when source documentation cannot be verified
- Say "I cannot access this source" when verification source is unavailable
- Mark findings as MANUAL VERIFICATION REQUIRED when sources are inaccessible

**MUST NOT:**
- Speculate about whether a fact is correct without proof
- Make assumptions about source content without reading it
- Mark facts as VERIFIED without consulting their cited sources

---

### 3. Citation Requirements (MANDATORY)

**MUST:**
- Include precise source reference and URL in verification evidence
- Link to official documentation sources used for verification
- Specify exact sections where claims are verified or disproven
- Include verbatim excerpts from sources as proof

**MUST NOT:**
- Perform verification without documenting the source consulted
- Reference sources by name only without URLs
- Archive disproven findings without citing contradicting evidence

---

### 4. Documentation Source Priority (MANDATORY)

**When verifying facts, prioritize sources in this order:**

1. Official project documentation
2. Official API references
3. Official language/framework specifications
4. Official GitHub repositories and READMEs
5. Official release notes and changelogs

**MUST:**
- Start verification with the highest priority source available
- Clearly document which source level verified or disproved the claim

**MUST NOT:**
- Treat community forums or unofficial blogs as proof
- Skip higher priority sources when available
- Use general knowledge as verification evidence

---

### 5. When Documentation is Unavailable (MANDATORY)

**When you cannot find official documentation to verify a claim:**

**MUST:**
- Explicitly state: "Official documentation could not be found for this claim"
- Indicate which sources you consulted
- Mark finding as MANUAL VERIFICATION REQUIRED
- Do not mark findings as VERIFIED without proof

**MUST NOT:**
- Proceed as if documented verification is available
- Present unverified assumptions as verified facts
- Hide the lack of documentation from the record

---

## Verification Workflow

### 1. Locate and Read Finding

1. Determine fact file path from topic/subtopic
2. Read fact file and locate the specified FINDING
3. Extract all claims from the finding
4. Retrieve source URL from fact metadata

### 2. Fetch Source and Gather Evidence

1. **For documentation claims:** Use WebFetch or WebSearch to load source content fresh
2. **For test/experimental claims:** Execute or reproduce the test/procedure that proves/disproves the claim
3. **For API claims:** Make actual API calls (if possible) or fetch live documentation
4. Compare fact claims against actual source content or test output
5. Check source/documentation publication dates for currency
6. **Gather all proof text/evidence before proceeding** - collect verbatim excerpts, test output, API responses, etc. for every claim
7. Document any discrepancies

### 3. Determine Verification Status (In Memory, No File Updates Yet)

Analyze all gathered evidence and determine status:

**VERIFIED:** All claims match source content exactly
- Status: VERIFIED
- Reason: (from evidence comparison)

**DISPROVEN:** Claims contradict official source documentation
- Status: DISPROVEN
- Archive destination: `-disproven.md` file
- Reason: (from evidence comparison)

**MANUAL VERIFICATION REQUIRED:** Source cannot be accessed automatically
- Status: MANUAL VERIFICATION REQUIRED
- Reason: (specific access limitation encountered)

### 4. Create Verification Working Document for Finding

Once status is determined and all evidence is gathered:

1. **Create if not exists:** `.memory/[topic]/[topic]-[subtopic]-verification.md` (or `.memory/[topic]/[topic]-verification.md` for main topic)
2. **Append complete verification entry** with all required sections

**DO NOT create or modify the working document until evidence gathering is complete.**

**Verification Working Document Entry Format:**

```markdown
### FINDING-YYYY-MM-DD-N Verification

**Date Verified:** YYYY-MM-DD
**Source:** [source-url]
**Source Publication Date:** YYYY-MM-DD (or current if updated regularly)
**Method:** WebFetch/WebSearch/Testing
**Status:** VERIFIED/DISPROVEN/MANUAL VERIFICATION REQUIRED

**Claims Verified:**
- Claim 1: [concise verification result]
- Claim 2: [concise verification result]

**Evidence:**
The following proof from the authoritative source confirms or contradicts each claim:

*Claim 1:*
> [Verbatim excerpt from documentation, test output, API response, or experimental result proving or disproving this specific claim]
Source section/location: [Document section, test file location, or API endpoint where result appears]

*Claim 2:*
> [Verbatim excerpt from documentation, test output, API response, or experimental result proving or disproving this specific claim]
Source section/location: [Document section, test file location, or API endpoint where result appears]

[If DISPROVEN: Detailed explanation of how source contradicts the finding, including relevant quotes or test output]
[If MANUAL: Specific explanation of verification limitation, and what type of verification would be required instead]
```

### 5. Archive or Update Fact File (Final Step)

Only after verification working document is complete, update the primary fact file:

1. **If VERIFIED:** Add verification tag to finding: `[VERIFIED on YYYY-MM-DD by [source-url]]`
2. **If DISPROVEN:** Move finding to `-disproven.md` archive file with full disproof details
3. **If MANUAL:** Add note in fact file: `[MANUAL VERIFICATION REQUIRED - reason]`

**Marking a fact as verified is the LAST step, after evidence documentation is complete.**

---

## Mandatory Verification Standards

### Source Fetching or Testing

- Use WebFetch or WebSearch for documentation claims
- Load source content fresh (no cached assumptions or cached test results)
- Verify individual claims against actual authoritative source content or test output
- Verify source publication dates (for documentation)
- Verify test/experimental procedures are still valid

### Content Comparison

- Compare fact statement against source content or test output directly
- Not just checking URL/source existence
- Verify technical accuracy, specifications, behaviors
- Validate test output against expected results and findings

### Currency Checking

- Review source publication dates (for documentation)
- Verify test/experimental procedures are still valid
- Flag if source appears outdated
- Note if source cannot be accessed or test cannot be reproduced

### Evidence Capture (MANDATORY)

- Capture verbatim excerpts, direct quotes, test output, or API response text from authoritative sources
- Each claim must have corresponding proof text/output from the source
- Include source section/URL fragment, test file location, or API endpoint identifying where proof appears
- For DISPROVEN findings: include exact contradicting text from source or test output showing failure
- For MANUAL VERIFICATION findings: document the specific reason verification wasn't possible
- Evidence must be sufficient for independent audit of the verification without re-running test or re-reading source
- Do NOT use paraphrases, summaries, or interpretations—use direct quotations or unmodified output

### No Batch Verification

- Each finding verified independently
- Fresh fetch/test per finding (no assumptions carry over from previous verifications)
- Complete verification before moving to next finding

---

## Error Handling

**Source Unreachable:**
- Tag as `[MANUAL VERIFICATION REQUIRED - source unreachable]`
- Document which source failed
- List what claims could not be verified

**Partial Verification:**
- Some claims verifiable, others not
- Document which claims verified against which sources
- Tag as `[PARTIALLY VERIFIED - see finding for details]`

**Conflicting Sources:**
- Document all sources and their claims
- Tag as `[REQUIRES CLARIFICATION - sources conflict]`
- Preserve full context for manual review

---

## Compliance Verification

Before completing verification:

- [ ] Specified finding was located in correct memory file?
- [ ] Source URL was extracted from finding metadata?
- [ ] Official source was fetched using WebFetch or WebSearch, OR test/procedure was executed?
- [ ] All claims in finding were checked against source content or test output?
- [ ] Source publication date was reviewed and documented for currency?
- [ ] **ALL evidence was gathered before any file updates?**
- [ ] Verification status was determined (VERIFIED/DISPROVEN/MANUAL)?
- [ ] **Verification working document was created/updated with complete evidence?**
- [ ] Verification entry includes all required sections (date, source, method, status, claims, evidence)?
- [ ] Evidence section contains verbatim excerpts from official source for EACH claim?
- [ ] Direct quotations were used, NOT paraphrases or summaries?
- [ ] Source section/URL fragment documented for each excerpt?
- [ ] **Fact file was updated with appropriate verification tag (LAST STEP)?**
- [ ] Disproven findings were archived to `-disproven.md` with full contradicting evidence?
- [ ] Index was updated if fact files changed?
- [ ] Verification report provided with detailed results?

**If ANY answer is "No":**
- Complete the missing verification step
- **Critical:** Do NOT tag facts in the primary fact file until the working document entry is complete
- These are mandatory standards
