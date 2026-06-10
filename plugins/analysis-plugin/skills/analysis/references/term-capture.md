# Term Capture and Extraction Guidelines

**This file is loaded when: You need detailed guidance on capturing, extracting, and maintaining domain terms in analysis workflows.**

---

# Embedded Rules

## Documentation-First Response Requirements (from /src/claude/rules/documentation-first.md)

### 1. Documentation Consultation (MANDATORY)

**MUST:**
- Search for and reference official documentation sources when defining terms
- Verify term definitions against authoritative sources (industry standards, official docs, published specifications)
- Prioritize official definitions over assumed or colloquial usage

**MUST NOT:**
- Rely solely on general knowledge or training data
- Create terms without verifying against official sources
- Skip documentation research even for seemingly standard terms

---

### 2. No Assumptions or Speculation (MANDATORY)

**MUST:**
- Explicitly state when a term's official definition cannot be verified through documentation
- Say "definition could not be verified" when uncertain about authoritative source
- Ask for clarification about term scope rather than assuming

**MUST NOT:**
- Speculate about what a term means without official source
- Make assumptions about technical terminology without documentation
- Define terms using only training data without verification

---

### 4. Documentation Source Priority (MANDATORY)

**When capturing terms, prioritize definition sources in this order:**

1. Official project/technology documentation
2. Official API references
3. Official standards and specifications
4. Official GitHub repositories and READMEs
5. Official release notes and documentation

**MUST:**
- Start with the highest priority source available
- Clearly indicate which source level you are citing

**MUST NOT:**
- Treat community forums or unofficial blogs as authoritative for term definitions
- Skip higher priority sources when available
- Use general knowledge as primary term source

---

## Literal Specification Compliance (from /src/claude/rules/literal-specification.md)

**MUST:**
- Follow TERM-YYYY-MM-DD-N format precisely (no variations)
- Include all required fields: definition, scope, sources, related-terms
- Preserve exact field order as specified in template
- Match the template structure character-for-character

**MUST NOT:**
- Add fields to the term template beyond specification
- Add metadata or sections not in specification
- Modify the term format for convenience
- Bundle multiple concepts into a single term (each term = singular scope)

---

## Existing Rules

### Define Terms with Singular Scope

When you create a term, define it as a semantic concept label for a single coherent idea. Do not create terms that bundle multiple related concepts into one entry.

**Use these characteristics to guide your term creation:**
- **Semantic meaning**: When you label a concept, ensure it labels a coherent idea, not just an access point
- **Fine-grained scope**: Create each term to define ONE clear concept
- **Hierarchical**: Keep general principles separate from specific implementations
- **Independently referenceable**: Create each term as a standalone entry with complete context

**Structure term hierarchies like this example:**
```
General principle:    REST API
├── GitHub-specific:  GitHub REST API
└── GitHub-specific:  GitHub GraphQL API
                      GraphQL API (separate from REST API)
                      GitHub API (parent umbrella concept)
```

**Do NOT bundle concepts into a single term:**
- ❌ "REST API / GraphQL API" (bundles two concepts)
- ✅ Create separately: "REST API", "GraphQL API", "GitHub REST API", "GitHub GraphQL API"

---

## Term File Location and Naming

### Where to Store Terms

When you extract terms from facts, maintain a central terms file in the workspace root `.memory/` directory:

**CORRECT location:**
```
.memory/[topic]/[topic]-terms.md
```

Example: `.memory/github-api/github-api-terms.md`

**MANDATORY: Do NOT create terms files in these wrong locations:**
- ❌ `src/claude/projects/-workspaces-[workspace-name]/memory/` (WRONG)
- ❌ `.claude/projects/...` (WRONG)
- ❌ Any location other than workspace root `.memory/[topic]/` (WRONG)

### Consolidate Terms at Topic Level

When subtopics introduce new terms, add them to the main topic's terms file—do not create separate terms files for subtopics.

**Structure:**
```
.memory/github-api/github-api-terms.md       (main terms file - put all terms here)
.memory/github-api/github-api-facts.md       (main facts file)
.memory/github-api/github-api-subtopic/      (subtopic folder)
├── github-api-subtopic-facts.md             (contributes terms to parent)
└── (DO NOT create github-api-subtopic-terms.md)
```

---

## Term Authority and Source Verification (MANDATORY)

When you create or maintain a term, consult authoritative sources and distinguish between official/industry standard terms and internal project terms.

### Source Hierarchy for Term Authority

When defining a term for a concept, prioritize sources in this order:

1. **Industry Standard Terms (Highest Authority)**
   - Official technical specifications (RFC, OASIS, W3C, etc.)
   - Standardized glossaries (IEEE, ISO, etc.)
   - Consensus definitions in official documentation
   - Examples: REST API, GraphQL, OAuth, JWT

2. **Official Third-Party Terms (High Authority)**
   - Official product/service documentation (GitHub, Docker, Kubernetes, etc.)
   - Official API references and specifications
   - Official language/framework documentation
   - Examples: GitHub Pull Request, Docker Container, Kubernetes Pod

3. **Internal/Project-Specific Terms (Lower Authority)**
   - Project documentation and design decisions
   - Team conventions and terminology
   - Internal domain concepts without external standards
   - Created ONLY when no industry standard or official term exists

### Term Creation Requirements

**Before creating a term, you MUST:**

1. **Check for existing standard terminology**
   - Search official documentation and specifications for the concept
   - Consult industry glossaries and standards
   - Review official API references for the service/product
   - Only proceed to step 2 if no authoritative term is found

2. **If an official or industry standard term exists:**
   - Use that term exactly as defined in the authoritative source
   - Cite the official source in the term's Sources table
   - Include the authoritative definition, not your interpretation
   - Link to the official documentation

3. **If no standard term exists, create an internal term:**
   - Document that this is an internal/project-specific term
   - Provide clear scope boundaries to prevent confusion
   - Cite project documentation or design decisions as sources
   - Mark as "Internal Term" in documentation

**MUST NOT create a term if:**
- An industry standard term already exists for the concept
- An official term from the canonical source documentation exists
- A different but equivalent term is already in use (consolidate instead)

### Fast Path: Terms from Official Documentation Sources

When facts are extracted from official documentation, the documentation itself supplies the correct terminology. This creates a fast-path workflow:

**When facts come from official documentation:**
1. Extract the terminology used in the official documentation (this IS the canonical source)
2. Cite the official documentation as the term's primary source
3. Verify that terminology against other industry sources to confirm correct usage
4. Create the term with the official documentation as the canonical source

**Example workflow:**
- Fact extracted from GitHub's official API documentation mentions "Pull Request"
- GitHub's official docs define what a Pull Request is
- Verify "Pull Request" is the correct term by checking other sources (GitHub GraphQL API docs, REST API docs, GitHub's glossary)
- Create term "Pull Request" with source: https://docs.github.com/pull-requests (the official documentation)
- Verification: Confirmed usage across GitHub's official documentation sources

This workflow eliminates the need to search for standard terminology when the source documentation already provides authoritative definitions.

### Sources: Definition vs. Usage

**Distinguish between two concepts:**

- **Canonical Sources** (go in Sources table): Authoritative documents that *define* the term
  - Official specification that defines the concept
  - Official API documentation defining the term
  - Standard glossary entry for the concept
  - Project documentation establishing the internal term

- **Usage References** (go in "Used in facts" / "Referenced By"): Facts and findings that *use or reference* the term
  - Facts introducing or discussing the concept
  - Findings that depend on understanding this term
  - Evidence of the term's relevance to the topic

The Sources table in the glossary template references canonical definitions, not usage locations.

### Verification Workflow for Sources

When you verify a term, authenticate its sources:

**During verification:**
1. Read the canonical source documents listed in Sources table
2. Confirm the term definition matches the source exactly
3. Verify the scope boundaries align with the authoritative definition
4. Document verification with link to source section
5. For internal terms: Confirm the project documentation clearly establishes the term

**Example verification:**
```markdown
| [Official GraphQL Specification](https://spec.graphql.org/) | VERIFIED | Verified 2026-03-23 against official specification section 3.1 |
| [GitHub GraphQL API Docs](https://docs.github.com/graphql) | VERIFIED | Verified 2026-03-23 against official documentation |
```

---

## Term Entry Format (MANDATORY)

### Create Term Entries Using This Format

When you create a term, use this exact structure:

```markdown
### TERM-[topic-slug]-[YYYY-MM-DD-N]

**Term:** [Term Name]

**Definition:** [One or more sentences defining the concept]

**Source:** [Canonical source that defines the term - official documentation URL, specification, or project documentation]

**Scope:** [Singular concept statement - what this term covers and what it does NOT cover]

**Key attributes:**
- [Attribute 1]: [Description]
- [Attribute 2]: [Description]

**Related terms:** [TERM-ID], [TERM-ID], [Concept Name (not yet defined)]

**Used in facts:**
- [FINDING-2026-03-22-1](path/to/fact-file.md#finding anchor) - Finding Name
- [FINDING-2026-03-22-5](path/to/fact-file.md#finding anchor) - Another Finding Name

**Verified:** [NOT YET VERIFIED - requires verification workflow via /verify-term skill]

**Captured:** YYYY-MM-DD HH:MM
```

**Note:** This format is for initial term capture during research. Once terms are ready for indexing and publication, format them using the standardized glossary template provided in [term-indexing.md](term-indexing.md). The glossary format includes a complete "Sources" table, expanded "Description" section, bidirectional "See Also" links, and "Referenced By" backlinks.

When terms are ready for verification, invoke the `/verify-analysis term` skill which creates a verification working document containing verbatim evidence from authoritative sources backing up the verification.

### Field Requirements

When you create a term entry, populate each field with this requirement:

- **TERM-[topic-slug]-YYYY-MM-DD-N**: Use this unique identifier format (topic slug + date + sequence number)
- **Term**: Supply the semantic label for the concept (1-4 words)
- **Definition**: Write a clear explanation of what the term encompasses
- **Source**: Cite where you extracted this term from (FINDING-ID or direct source URL)
- **Scope**: Write an explicit statement of what this term covers and its boundaries (prevents conflation with related concepts)
- **Key attributes**: List 2-5 important characteristics that define this concept
- **Related terms**: Link to other term IDs this one connects to, and include placeholders for undefined concepts you'll create later
- **Used in facts**: Include backlinks to every fact that uses or introduces this term
- **Verified**: Always write "NOT YET VERIFIED - requires verification workflow" during capture phase (same requirement as facts)
- **Captured**: Record the timestamp when you created this term entry

### Example Term Entry

When you create a term, structure it like this example:

```markdown
### TERM-github-api-2026-03-22-4

**Term:** GitHub REST API

**Definition:** GitHub's REST (Representational State Transfer) implementation for API access. Uses HTTP methods (GET, POST, PUT, DELETE) with fixed endpoint paths. Each endpoint returns a structured response containing specific fields.

**Source:** https://tools.ietf.org/html/rfc7231#section-4.9 (extracted and confirmed via FINDING-2026-03-22-4)

**Scope:** Refers specifically to GitHub's REST API implementation. Does NOT include general REST API principles (see "REST API" term) or GitHub GraphQL API (see "GitHub GraphQL API" term).

**Key attributes:**
- **Endpoint-based**: Each operation is a specific HTTP endpoint (e.g., `/repos/{owner}/{repo}/pulls/{number}`)
- **Fixed response structure**: Cannot request specific fields; server returns all fields
- **HTTP semantics**: Uses GET, POST, PUT, DELETE, PATCH methods and status codes
- **Simpler for operations**: Straightforward for single-resource operations

**Related terms:** TERM-github-api-2026-03-22-3 (GitHub API), TERM-github-api-2026-03-22-7 (REST API), TERM-github-api-2026-03-22-5 (GitHub GraphQL API)

**Used in facts:**
- [FINDING-2026-03-22-4](github-api-facts.md#finding-2026-03-22-4) - GitHub REST API definition extracted
- [FINDING-2026-03-22-1](github-api-facts.md#finding-2026-03-22-1) - Pull Request mentions REST API

**Verified:** [NOT YET VERIFIED - requires verification workflow]

**Captured:** 2026-03-22 12:45
```

---

## Term Extraction Workflow

### Extract Terms Automatically When Facts Introduce Concepts

When you create a fact that introduces a new semantic concept, extract it as a term immediately.

**Determine whether to extract a term:**

Use these conditions to decide:
1. Does the fact define a new concept label with semantic meaning?
2. Should this concept be independently referenceable across the topic?
3. Does the concept have clear boundaries (singular scope)?
4. Might other facts reference this concept?

If all conditions are yes, extract a term.

**Extract when you identify these triggers:**
- ✅ Finding about "Pull Request" → Extract as term (singular semantic concept)
- ✅ Finding about "REST API" → Extract as term (general principle, cross-domain applicable)
- ✅ Finding about "Head Branch" → Extract as term (specific role in PR structure)
- ❌ Finding mentions "the number field" → Do NOT extract (too granular, attribute not concept)
- ❌ Finding mentions "API" casually → Do NOT extract unless it defines "API" as a concept

**Execute automatic extraction workflow:**

1. After you append a finding to a fact file
2. Identify whether the finding introduces a concept that should be a term
3. Create term entry in `[topic]-terms.md` (create file if it does not exist)
4. Add backlink in finding to new term (or add term reference if term already existed)
5. Update terms index

### Extract Terms On Demand

When the user explicitly requests term extraction from facts, use this workflow:

**Execute on-demand extraction workflow:**

1. Read the specified fact files
2. Scan for semantic concepts (not keywords)
3. For each concept:
   - Check whether term already exists in `[topic]-terms.md`
   - If new: Create term entry with complete definition, scope, and attributes
   - If existing: Update "Used in facts" backlinks with new findings
4. Update terms index
5. Report findings: how many terms created/updated, what relationships emerged

### Extracting Terms from Official Documentation

When facts come from official documentation (GitHub docs, API references, specifications), the documentation itself provides the authoritative terms:

**When extracting terms from official documentation sources:**

1. Use terminology exactly as presented in the official documentation
2. Cite the official documentation URL as the term's Source
3. The fact's source documentation IS the canonical term definition
4. During verification: Compare against other official sources to confirm consistent terminology usage
5. Create the term entry immediately after capturing the fact

**Example extraction:**
- Fact extracted from https://docs.github.com/pull-requests discussing "Pull Request" concept
- Extract term "Pull Request" (as named in official docs)
- Set Source: https://docs.github.com/pull-requests
- Verification workflow: Check GitHub REST/GraphQL docs for consistent "Pull Request" terminology usage
- Mark VERIFIED once terminology is confirmed consistent across official sources

This extraction approach leverages the official documentation's authority rather than searching for external definitions.

---

## Bidirectional Linking (MANDATORY)

When you link facts and terms, you must maintain two-way links for complete traceability.

### Add Term Links to Fact Entries

When you create a fact, add term references to the fact entry:

**Add this line to fact entries:**
```markdown
**Introduces term:** TERM-github-api-2026-03-22-1

**Uses terms:** TERM-github-api-2026-03-22-3, TERM-github-api-2026-03-22-5
```

**Link format requirements:**
- Write "**Introduces term:**" when the fact defines or first introduces this term
- Write "**Uses terms:**" when the fact uses existing terms without introducing them
- Use the complete TERM-ID for each link

### Add Fact Backlinks to Term Entries

When you maintain a term, keep its "Used in facts" section current:

**Update "Used in facts" whenever:**
- A new fact introduces or uses this term
- An existing fact is archived (remove it from the "Used in facts" list)

**Format backlinks like this:**
```markdown
**Used in facts:**
- [FINDING-2026-03-22-4](github-api-facts.md#finding-2026-03-22-4) - GitHub REST API definition
- [FINDING-2026-03-22-1](github-api-facts.md#finding-2026-03-22-1) - Pull Request mentions REST API
```

### Transitive Fact References Through Term Hierarchy

When a term extends or references another term (hierarchical parent-child relationship), facts that reference the child term automatically also reference the parent term.

**Example:** If GitHub REST API establishes GitHub API as its parent concept, then any fact using GitHub REST API implicitly also uses GitHub API. Update the parent term's "Used in facts" to include these transitive references.

**When updating "Used in facts" for parent terms:**
- Include facts that directly reference this term
- Include facts that reference any child term (as child term usage implies parent term usage)
- Mark transitive references to show which child term mediates the reference

**Example:**
```markdown
**Used in facts:**
- [FINDING-2026-03-22-10](github-api-facts.md#finding-2026-03-22-10) - Direct reference to GitHub API
- [FINDING-2026-03-22-4](github-api-facts.md#finding-2026-03-22-4) - Via GitHub REST API
- [FINDING-2026-03-22-5](github-api-facts.md#finding-2026-03-22-5) - Via GitHub GraphQL API
```

---

## Term Validation Criteria (MANDATORY)

When you create and maintain terms, apply the exact same validation requirements as you apply to facts.

### Verify Terms During Creation

Before finalizing a term entry, verify it meets these requirements:

**MUST have before creating a term:**
- Canonical source verification (industry standard or official documentation consulted)
- Clear, singular scope (what this term covers; what it does NOT cover)
- Source citation pointing to authoritative definition (not just usage location)
- Complete definition with context matching the authoritative source
- Key attributes that characterize the concept (2-5 attributes)
- Related terms listed (existing terms + placeholders for future related terms)
- Confirmation that no industry standard or official term already exists for this concept

**MUST NOT do when creating terms:**
- Create terms that bundle multiple concepts (violates singular scope)
- Create terms without clear source documentation
- Create terms that duplicate industry standard or official terminology
- Create terms without consulting authoritative sources first
- Create internal terms when official/industry standard terms exist
- Ignore existing standard terminology for a concept

### Run Verification Workflow

When you engage the verification workflow, treat terms the same as facts. Use the `/verify-analysis term` skill to verify individual terms:

**During verification phase:**
- Invoke `/verify-analysis term [topic] [subtopic] [term-id]` skill for the term
- Skill fetches authoritative definition sources
- Skill verifies term definition matches authoritative source exactly
- Skill verifies scope boundaries align with source scope
- Skill confirms consistent usage across related official sources
- Skill creates verification working document with verbatim evidence
- Skill archives disputed terms to `-disproven.md`

**Verification working document captures:**
- Verbatim excerpts from authoritative definition sources
- Proof that term definition matches source definition
- Proof that scope boundaries align with authoritative scope
- Evidence of terminology consistency across related sources
- Full context for auditing the verification independently

**After verification:**
- Review verification working document report
- Term file is updated with verification status by skill
- Central index automatically includes newly verified terms
- Disputed findings are archived with contradiction evidence

### Archive Disproven Terms

When you discover a term is incorrect or misconstrued, archive it immediately—never delete it.

**Archive disproven terms using this format:**

Create or update `.memory/[topic]/[topic]-terms-disproven.md` with:

```markdown
### TERM-github-api-2026-03-22-12 [DISPROVEN]

**Original term:** [Term Name]

**Disproven:** 2026-03-22 15:00

**Reason:** [Explanation of why this term was inaccurate]

**Evidence:** [References showing the term was incorrect]

[Original definition and attributes...]

**Disproven by finding:** FINDING-YYYY-MM-DD-N
```

---

## Terms Index Maintenance (MANDATORY)

When you manage terms, maintain an index file at the topic level.

### Create and Update Terms Index

Maintain this index file: `.memory/[topic]/[topic]-terms-index.md`

**Update the index after each significant operation:**
- New term created
- Term verified
- Term archived
- Backlinks updated

**Structure the index like this:**
```markdown
# [Topic] Terms Index

**Last Updated:** YYYY-MM-DD HH:MM

---

## Terms Summary

- **Total terms:** N
- **Verified:** N
- **Pending verification:** N
- **Archived (disproven):** N

---

## Terms by Category

### [Category 1]

| Term | ID | Verified | Used in Facts |
|------|----|-----------|----|
| [Term 1](path/to/terms.md#term anchor) | TERM-ID-1 | ✅ | 3 facts |
| [Term 2](path/to/terms.md#term anchor) | TERM-ID-2 | ⏳ | 1 fact |

### [Category 2]

| Term | ID | Verified | Used in Facts |
|------|----|-----------|----|
| [Term 3](path/to/terms.md#term anchor) | TERM-ID-3 | ✅ | 5 facts |

---

## Term Relationships

[When you maintain multiple related terms, document their hierarchy]

**Example hierarchy:**
```
GitHub API (parent)
├── GitHub REST API
└── GitHub GraphQL API

REST API (general principle)
GraphQL API (general principle)
```

---

## Verification Status

| Term | Status | Last Verified | Source |
|------|--------|---------------|----|
| TERM-github-api-2026-03-22-1 | ✅ VERIFIED | 2026-03-22 14:30 | [source-url] |
| TERM-github-api-2026-03-22-4 | ⏳ PENDING | — | FINDING-2026-03-22-4 |
```

---

## Integration with Analysis Workflow

### Where Term Extraction Fits in Your Process

Execute term extraction as step 1.5 in the analysis workflow:

1. ✅ Capture Research in Fact Files (existing)
2. ✨ **Extract and Maintain Terms (THIS STEP)** ← You are here
   - Auto-extract terms from facts as created
   - Update bidirectional links
   - Maintain terms index
3. ✅ Archive Disproven Findings (existing)
4. ✅ Update Analysis Index (existing)
5. ✅ Create Final Output (existing)
6. ✅ Operation Logging (existing)

### Create Terms File When Needed

Create `[topic]-terms.md` when:
- You extract your first term from a finding
- User explicitly requests term extraction
- Topic has 2+ semantic concepts worth indexing

### Keep Terms Current

Update existing terms when:
- New facts are added that use or reference the term
- Clarifications refine the term definition (append as new term referencing original)
- Verification updates the term's status
- Related terms are discovered

---

## File Size Management for Terms

**Monitor term file size:**
- **Maximum:** 30,000 characters (~7,500 tokens)
- **Action trigger:** When you would add terms that would exceed this limit

**When you exceed the threshold, execute this process:**
1. Create subtopic terms file: `.memory/[topic]/[topic]-[subtopic]/[topic]-[subtopic]-terms.md`
2. Move related term entries to subtopic file
3. Update both files' indices to cross-reference
4. Update main topic terms index with subtopic reference

---

## MUST/MUST NOT Summary

**During term capture, you MUST:**
- Consult authoritative sources (industry standards, official documentation) before creating terms
- Extract terms with singular, clear scope
- Include complete source citation pointing to canonical definition
- Confirm no industry standard or official term already exists before creating a term
- Define key attributes distinct from keywords (2-5 attributes)
- Link bidirectionally with facts
- Update terms index after each change
- Apply exact same validation criteria as facts
- Archive disproven terms without deletion
- Follow standardized term entry template from [term-indexing.md](term-indexing.md)
- Maintain central `index-terms.md` with only VERIFIED terms
- Monitor term index file sizes (maximum 500 lines per file)
- Use alphabetical ordering in term index files
- Include transitive fact references when a term has child terms

**During term capture, you MUST NOT:**
- Create terms that bundle multiple concepts
- Create terms without clear scope boundaries
- Create terms that duplicate industry standard or official terminology
- Skip source citations or cite only usage locations
- Create separate terms files for subtopics
- Edit existing terms during research phase (append clarifications instead)
- Mark terms as verified before running verification workflow
- Delete or lose bidirectional links
- Forget transitive references when updating parent term "Used in facts"
- Create internal terms when official or industry standard terms exist
