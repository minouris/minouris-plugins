---
name: verify-term
description: Verify individual terms against authoritative source definitions with sub-agent autonomy
allowed-tools: Read, Edit, Write, WebFetch, WebSearch
context: fork
---

# Verify Term Skill

Verify individual terms against authoritative definition sources and update memory files with verification status.

## Overview

This skill executes term verification at the individual term level, designed to work as a delegated sub-agent task. It:
- Retrieves a specific term from a memory file
- Fetches authoritative definition sources (official documentation, specifications, standards) and compares the term definition
- Verifies scope boundaries align with authoritative definitions
- Confirms term usage is correct and consistent across official sources
- Tags terms as VERIFIED or marks for manual verification
- Archives disputed terms immediately
- Updates term files atomically

**What counts as authoritative "proof" for terms:**
- Official documentation that defines the term
- Official API specifications and references
- Technical specifications and published standards (RFC, W3C, ISO, etc.)
- Official glossaries and terminology references
- Related official documentation confirming consistent terminology usage

## Usage

```
/verify-term <topic> [<subtopic>] <term-id>
```

### Parameters

- **topic** (required): Topic slug (e.g., `github-api`)
- **subtopic** (optional): Subtopic folder name (e.g., `github-api-actions`)
- **term-id** (required): Term identifier or term name (e.g., `TERM-2026-03-11-06` or `Pull Request`)

### Examples

```
/verify-term github-api TERM-2026-03-11-06
/verify-term github-api github-api-actions TERM-2026-03-22-04
/verify-term github-api "Pull Request"
```

## Verification Workflow

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

### 4. Create and Populate Verification Working Document

Once status is determined and all evidence is gathered:

1. **Create if not exists:** `.memory/[topic]/[topic]-[subtopic]-term-verification.md` (or `.memory/[topic]/[topic]-term-verification.md` for main topic)
2. **Append complete verification entry** with all required sections:
   - Term name and ID
   - Date, sources from Sources table
   - Verification method
   - Status
   - Definition verification results
   - Scope verification results
   - **Full proof text evidence** (verbatim excerpts from authoritative sources)
   - Consistency check across related sources
   - Discrepancies or dispute explanations

**DO NOT create or modify the working document until evidence gathering is complete.**

### 5. Archive or Update Term File (Final Step)

Only after verification working document is complete, update the primary term file:

1. **If VERIFIED:** Mark in term entry: `**Verified:** VERIFIED on YYYY-MM-DD by [source-urls]`
2. **If DISPUTED:** Move term to `-disproven.md` archive file with full dispute details
3. **If MANUAL:** Add note in term entry: `**Verified:** MANUAL VERIFICATION REQUIRED - reason`

**Marking a term as verified (or otherwise tagged) is the LAST step, after evidence documentation is complete.**

### 6. Report Results

Return detailed verification report including:
- Term name and ID
- Sources checked and verification results for each
- Verification status and specific results for definition and scope
- Consistency check results across related sources
- Any manual verification notes or dispute evidence

---

## Verification Working Document Entry Format

Reference template for the complete verification entry structure:

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

## Mandatory Verification Standards

**Source Fetching:**
- Use WebFetch or WebSearch for official documentation
- Load source content fresh (no cached assumptions)
- Verify against current version of authoritative sources
- Check publication/update dates for currency

**Definition Comparison:**
- Compare term definition against source definition directly
- Not just checking URL/source existence
- Verify technical accuracy matches authoritative terminology
- Validate scope boundaries align with source scope
- Check consistency across related official sources

**Currency Checking:**
- Review source publication/update dates
- Flag if source appears outdated or superseded
- Note if source cannot be accessed
- Check for superseding terminology or updated definitions

**Evidence Capture (MANDATORY):**
- Capture verbatim excerpts from authoritative sources defining the term
- Each verification check must have corresponding proof text from the source
- Include source section/URL fragment identifying where proof appears
- For DISPUTED findings: include exact contradicting text from source showing discrepancy
- For MANUAL VERIFICATION findings: document the specific reason verification wasn't possible
- Evidence must be sufficient for independent audit without re-reading source
- Do NOT use paraphrases, summaries, or interpretations—use direct quotations

**Consistency Verification:**
- For official product terms: Check consistency across product documentation (REST API docs, GraphQL docs, main docs)
- For industry standard terms: Verify consistent usage across related specifications
- Document which sources confirm terminology consistency
- Note any variations in terminology usage

## Error Handling

**Source Unreachable:**
- Tag as `[MANUAL VERIFICATION REQUIRED - source unreachable]`
- Document which sources failed
- List which aspects of the term could not be verified

**Partial Verification:**
- Some claims verifiable, others not
- Document which claims (definition, scope, etc.) verified against which sources
- Tag as `[PARTIALLY VERIFIED - see verification working document for details]`

**Conflicting Definitions:**
- Document all sources and their definitions
- Tag as `[DISPUTED - conflicting definitions found]`
- Include evidence from each source showing contradiction

**Superseded Terms:**
- If official source shows term is superseded or deprecated
- Document the replacement term
- Tag as `[DISPUTED - term superseded by [replacement term]]`

## Integration with Term Capture Workflow

This skill is invoked upon term creation:
1. Term is appended to memory file with `**Verified:** NOT YET VERIFIED` tag
2. `/verify-term` skill is invoked as background agent
3. Verification working document is created/updated with detailed verification entry
4. Term file is updated with verification tag from working document
5. Central term index is updated with verified term
6. Verification result reported to calling context

---

## Tool Requirements

- **Read**: Access term files and memory structure
- **Edit**: Update term files with verification tags
- **Write**: Create archive files for disputed terms
- **WebFetch**: Fetch official documentation sources
- **WebSearch**: Find authoritative sources when WebFetch fails

## Compliance Verification

Before completing verification:

- [ ] Specified term was located in correct memory file?
- [ ] All sources from term's Sources table were identified?
- [ ] Term definition and scope were extracted from term entry?
- [ ] Official/authoritative definition sources were fetched using WebFetch or WebSearch?
- [ ] Term definition was compared against authoritative source definition?
- [ ] Term scope boundaries were verified against source scope?
- [ ] Consistency was checked across related official sources?
- [ ] Source publication/update dates were reviewed for currency?
- [ ] **ALL evidence was gathered before any file updates?**
- [ ] Verification status was determined (VERIFIED/DISPUTED/MANUAL)?
- [ ] **Verification working document was created/updated with complete evidence?**
- [ ] Verification entry includes all required sections (term name, sources, definition verification, scope verification, evidence)?
- [ ] Evidence section contains verbatim excerpts from authoritative sources?
- [ ] Direct quotations were used, NOT paraphrases or summaries?
- [ ] Source section/URL fragment documented for each excerpt?
- [ ] **Term file was updated with appropriate verification tag (LAST STEP)?**
- [ ] Disputed terms were archived to `-disproven.md` with full contradicting evidence?
- [ ] Central term index was updated with verified term?
- [ ] Verification report provided with detailed results?

**If ANY answer is "No":**
- Complete the missing verification step
- **Critical:** Do NOT tag terms in the primary term file until the working document entry is complete
- These are mandatory standards
