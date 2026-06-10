# Term Verification Workflow

**This file is loaded when: You need detailed guidance on verifying individual terms against authoritative definition sources.**

---

# Embedded Rules

## Documentation-First Response Requirements (from /src/claude/rules/documentation-first.md)

**Term verification IS pure documentation-first operation. You must consult authoritative sources to verify every term definition.**

### 1. Documentation Consultation (MANDATORY)

**MUST:**
- Search for and reference official documentation sources for every term definition
- Verify each term against authoritative definition sources
- Prioritize official documentation, standards, and specifications over general knowledge

**MUST NOT:**
- Rely on general knowledge or training data to verify terms
- Provide term verification without consulting official sources
- Skip documentation research assuming a term is standard

---

### 2. No Assumptions or Speculation (MANDATORY)

**MUST:**
- Explicitly state when authoritative source documentation cannot be verified
- Say "I cannot access this source" when definition source is unavailable
- Mark terms as MANUAL VERIFICATION REQUIRED when sources are inaccessible

**MUST NOT:**
- Speculate about whether a term definition is correct without proof
- Make assumptions about what official sources say without reading them
- Mark terms as VERIFIED without consulting authoritative definition sources

---

### 3. Citation Requirements (MANDATORY)

**MUST:**
- Include precise source reference and URL in verification evidence
- Link to official documentation sources used for verification
- Specify exact sections where term definitions are verified or disputed
- Include verbatim excerpts from sources proving term definitions

**MUST NOT:**
- Perform verification without documenting the source consulted
- Reference sources by name only without URLs
- Archive disputed terms without citing contradicting definition evidence

---

### 4. Documentation Source Priority (MANDATORY)

**When verifying terms, prioritize definition sources in this order:**

1. Official project documentation (if project-specific term)
2. Official specifications and standards (RFC, W3C, ISO, etc.)
3. Official API references and style guides
4. Official GitHub repositories and READMEs
5. Official technical reference documentation

**MUST:**
- Start verification with the highest priority source available
- Clearly document which source level defined the term

**MUST NOT:**
- Treat community forums or unofficial tutorials as authoritative definitions
- Skip higher priority sources when available
- Use general knowledge as the term definition source

---

### 5. When Documentation is Unavailable (MANDATORY)

**When you cannot find official documentation for a term definition:**

**MUST:**
- Explicitly state: "Official definition source could not be found for this term"
- Indicate which sources you consulted
- Mark term as MANUAL VERIFICATION REQUIRED
- Do not mark terms as VERIFIED without documentation proof

**MUST NOT:**
- Proceed as if documented definition is available
- Present unverified assumptions as verified term definitions
- Hide the lack of official documentation from the record

---

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

### Source Fetching

- Use WebFetch or WebSearch for official documentation
- Load source content fresh (no cached assumptions)
- Verify against current version of authoritative sources
- Check publication/update dates for currency

### Definition Comparison

- Compare term definition against source definition directly
- Not just checking URL/source existence
- Verify technical accuracy matches authoritative terminology
- Validate scope boundaries align with source scope
- Check consistency across related official sources

### Currency Checking

- Review source publication/update dates
- Flag if source appears outdated or superseded
- Note if source cannot be accessed
- Check for superseding terminology or updated definitions

### Evidence Capture (MANDATORY)

- Capture verbatim excerpts from authoritative sources defining the term
- Each verification check must have corresponding proof text from the source
- Include source section/URL fragment identifying where proof appears
- For DISPUTED findings: include exact contradicting text from source showing discrepancy
- For MANUAL VERIFICATION findings: document the specific reason verification wasn't possible
- Evidence must be sufficient for independent audit without re-reading source
- Do NOT use paraphrases, summaries, or interpretations—use direct quotations

### Consistency Verification

- For official product terms: Check consistency across product documentation (REST API docs, GraphQL docs, main docs)
- For industry standard terms: Verify consistent usage across related specifications
- Document which sources confirm terminology consistency
- Note any variations in terminology usage

---

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

---

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
