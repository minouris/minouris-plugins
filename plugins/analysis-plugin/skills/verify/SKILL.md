---
name: verify
description: Verify research findings or terms against authoritative sources with sub-agent autonomy
allowed-tools: Read, Edit, Write, WebFetch, WebSearch
context: fork
---

# Verify Skill

Verify individual research findings or terms against authoritative sources and update memory files with verification status.

## Overview

This skill executes verification at the individual finding or term level, designed to work as a delegated sub-agent task. It:
- Retrieves a specific finding or term from a memory file
- Fetches authoritative sources and compares claims/definitions
- Tags findings/terms as VERIFIED or marks for manual verification
- Archives disproven findings/terms immediately
- Updates fact/term files atomically
- Creates verification working documents with verbatim evidence

**What counts as authoritative "proof":**
- Official documentation and specifications
- Output from reproducible local tests or scripts
- Results from experimentation against live APIs (with command/test output)
- Technical specifications and published standards
- Direct observations from reproducible procedures

## Usage

```
/verify fact <topic> [<subtopic>] <finding-id>
/verify term <topic> [<subtopic>] <term-id>
```

### Parameters

- **verification-type** (required): `fact` or `term`
- **topic** (required): Topic slug (e.g., `github-api`)
- **subtopic** (optional): Subtopic folder name (e.g., `github-api-authentication`)
- **id** (required): Finding ID (e.g., `FINDING-2026-03-11-06`) or Term ID/name (e.g., `TERM-2026-03-11-06` or `Pull Request`)

### Examples

```
/verify fact github-api FINDING-2026-03-11-06
/verify fact github-api github-api-authentication FINDING-2026-03-11-16
/verify term github-api TERM-2026-03-11-06
/verify term github-api github-api-actions TERM-2026-03-22-04
/verify term github-api "Pull Request"
```

---

## FACT VERIFICATION WORKFLOW

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

## TERM VERIFICATION WORKFLOW

### 1. Locate and Read Term

1. Determine term file path from topic/subtopic
2. Read term file and locate the specified term entry
3. Extract all sources from the term's Sources table
4. Extract term definition, scope, and key attributes
5. Validate that sources point to authoritative definition documents

### 2. Fetch Definition Sources and Verify Claims

1. **For industry standard terms:** Fetch the official specification (RFC, W3C, ISO, etc.)
2. **For official product terms:** Fetch official documentation from product provider
3. **For internal terms:** Verify project documentation establishes the term
4. Compare term definition against source definition
5. Verify scope boundaries match authoritative boundaries
6. Check that term usage is consistent across related official sources
7. **Gather all proof text/evidence before proceeding** - collect verbatim excerpts, definition passages, scope statements for every source
8. Document any discrepancies between term definition and source definition

### 3. Determine Verification Status (In Memory, No File Updates Yet)

Analyze all gathered evidence and determine status:

**VERIFIED:** Term definition and scope match authoritative sources exactly
- Status: VERIFIED
- Reason: (from evidence comparison)
- Consistent across: (list of sources where terminology is consistent)

**DISPUTED:** Term definition contradicts authoritative source documentation
- Status: DISPUTED
- Archive destination: `-disproven.md` file
- Reason: (from evidence comparison)

**MANUAL VERIFICATION REQUIRED:** Source cannot be accessed automatically
- Status: MANUAL VERIFICATION REQUIRED
- Reason: (specific access limitation encountered)

### 4. Create Verification Working Document for Term

Once status is determined and all evidence is gathered:

1. **Create if not exists:** `.memory/[topic]/[topic]-[subtopic]-term-verification.md` (or `.memory/[topic]/[topic]-term-verification.md` for main topic)
2. **Append complete verification entry** with all required sections

**DO NOT create or modify the working document until evidence gathering is complete.**

**Verification Working Document Entry Format:**

```markdown
### TERM-YYYY-MM-DD-N: [Term Name]

**Date Verified:** YYYY-MM-DD
**Sources Checked:**
- [Source 1 URL]
- [Source 2 URL]

**Method:** WebFetch/WebSearch
**Status:** VERIFIED/DISPUTED/MANUAL VERIFICATION REQUIRED

**Definition Verification:**
- **Claimed:** [Term definition from term entry]
- **Source Definition:** [Definition from authoritative source]
- **Result:** [VERIFIED/DISPUTED - explain match or discrepancy]

**Scope Verification:**
- **Claimed Scope:** [Scope statement from term entry]
- **Source Scope:** [Scope boundaries from authoritative source]
- **Result:** [VERIFIED/DISPUTED - explain match or discrepancy]

**Consistency Across Sources:**
- [Source 1]: terminology consistent - [brief note]
- [Source 2]: terminology consistent - [brief note]

**Evidence:**
The following proof from authoritative sources confirms or disputes the term definition:

*Definition:*
> [Verbatim excerpt from official documentation defining this term]
Source section/location: [Document section, repository location, or specification reference where definition appears]

*Scope Boundaries:*
> [Verbatim excerpt from official documentation describing scope or boundaries]
Source section/location: [Document section, repository location, or specification reference]

*Consistency Check:*
> [Verbatim excerpt from related official documentation confirming consistent usage]
Source: [Related official documentation URL]

[If DISPUTED: Detailed explanation of how official source contradicts the term definition, including relevant quotes showing the discrepancy]
[If MANUAL: Specific explanation of verification limitation, and what type of verification would be required instead]
```

### 5. Archive or Update Term File (Final Step)

Only after verification working document is complete, update the primary term file:

1. **If VERIFIED:** Mark in term entry: `**Verified:** VERIFIED on YYYY-MM-DD by [source-urls]`
2. **If DISPUTED:** Move term to `-disproven.md` archive file with full dispute details
3. **If MANUAL:** Add note in term entry: `**Verified:** MANUAL VERIFICATION REQUIRED - reason`

**Marking a term as verified is the LAST step, after evidence documentation is complete.**

---

## Mandatory Verification Standards

### Source Fetching or Testing

- Use WebFetch or WebSearch for documentation claims (facts) or definition sources (terms)
- Load source content fresh (no cached assumptions or cached test results)
- Verify individual claims/definitions against actual authoritative source content or test output
- For terms: Check publication/update dates for currency

### Content Comparison

**For Facts:**
- Compare fact statement against source content or test output directly
- Not just checking URL/source existence
- Verify technical accuracy, specifications, behaviors

**For Terms:**
- Compare term definition against source definition directly
- Not just checking URL/source existence
- Verify scope boundaries align with authoritative boundaries
- Check consistency across related official sources

### Evidence Capture (MANDATORY)

- Capture verbatim excerpts, direct quotes, test output, or API response text from authoritative sources
- Each claim/verification must have corresponding proof text/output from the source
- Include source section/URL fragment, test file location, or API endpoint identifying where proof appears
- For DISPROVEN/DISPUTED findings: include exact contradicting text from source or test output showing failure
- For MANUAL VERIFICATION findings: document the specific reason verification wasn't possible
- Evidence must be sufficient for independent audit of the verification without re-running test or re-reading source
- Do NOT use paraphrases, summaries, or interpretations—use direct quotations or unmodified output

### No Batch Verification

- Each finding/term verified independently
- Fresh fetch/test per finding/term (no assumptions carry over from previous verifications)
- Complete verification before moving to next item

---

## Error Handling

**Source Unreachable:**
- Tag as `[MANUAL VERIFICATION REQUIRED - source unreachable]`
- Document which source failed
- List which claims/aspects could not be verified

**Partial Verification:**
- Some claims/aspects verifiable, others not
- Document which claims verified against which sources
- Tag as `[PARTIALLY VERIFIED - see working document for details]`

**Conflicting Sources:**
- Document all sources and their claims/definitions
- Tag as `[REQUIRES CLARIFICATION - sources conflict]`
- Preserve full context for manual review

**Superseded Terms (Term Verification Only):**
- If official source shows term is superseded or deprecated
- Document the replacement term
- Tag as `[DISPUTED - term superseded by [replacement term]]`

---

## Integration with Workflows

### Fact Verification
This skill is invoked by fact-capture.md inline verification workflow:
1. Fact is appended to memory file with `[NOT YET VERIFIED]` tag
2. `/verify fact` skill is invoked as background agent
3. Verification working document is created/updated with detailed verification entry
4. Fact file is updated with verification tag from working document
5. Index is updated with new verified fact
6. Verification result reported to calling context

### Term Verification
This skill is invoked upon term creation:
1. Term is appended to memory file with `**Verified:** NOT YET VERIFIED` tag
2. `/verify term` skill is invoked as background agent
3. Verification working document is created/updated with detailed verification entry
4. Term file is updated with verification tag from working document
5. Central term index is updated with verified term
6. Verification result reported to calling context

---

## Tool Requirements

- **Read**: Access fact/term files and memory structure
- **Edit**: Update fact/term files with verification tags
- **Write**: Create archive files for disproven findings/disputed terms
- **WebFetch**: Fetch official documentation sources
- **WebSearch**: Find authoritative sources when WebFetch fails

## Compliance Verification

Before completing verification:

**Both Fact and Term Verification:**
- [ ] Specified finding/term was located in correct memory file?
- [ ] Source URL/sources were extracted from metadata?
- [ ] Official source was fetched using WebFetch or WebSearch, OR test/procedure was executed?
- [ ] **ALL evidence was gathered before any file updates?**
- [ ] Verification status was determined (VERIFIED/DISPROVEN-DISPUTED/MANUAL)?
- [ ] **Verification working document was created/updated with complete evidence?**
- [ ] Verification entry includes all required sections?
- [ ] Evidence section contains verbatim excerpts from official source?
- [ ] Direct quotations were used, NOT paraphrases or summaries?
- [ ] Source section/URL fragment documented for each excerpt?
- [ ] **Fact/term file was updated with appropriate verification tag (LAST STEP)?**
- [ ] Disproven/disputed items were archived to `-disproven.md` with full contradicting evidence?
- [ ] Index was updated if fact/term files changed?
- [ ] Verification report provided with detailed results?

**Fact-Specific:**
- [ ] All claims in finding were checked against source content or test output?
- [ ] Source publication date was reviewed and documented for currency?

**Term-Specific:**
- [ ] Term definition was compared against authoritative source definition?
- [ ] Term scope boundaries were verified against source scope?
- [ ] Consistency was checked across related official sources?

**If ANY answer is "No":**
- Complete the missing verification step
- **Critical:** Do NOT tag facts/terms in the primary files until the working document entry is complete
- These are mandatory standards
