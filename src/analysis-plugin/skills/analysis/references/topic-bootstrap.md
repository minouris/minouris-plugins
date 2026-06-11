# Topic Bootstrap Feature

**This reference file provides the topic bootstrap workflow for initializing a new research topic in the knowledge base.**

---

# Embedded Rules

## AI-Targeted Language Requirements (from /src/claude/rules/ai-targeted-language.md)

**MUST:**
- Write instructions directly to the AI agent (second person: "you")
- Use imperative commands addressing the AI
- Use consistent, direct imperatives: "MUST", "MUST NOT", "When you...", "Do not..."
- Use imperative mood ("Create", "Run", "Verify", "Use X", "Check Z")
- Use direct address ("When you create...", "You must...")
- Use unambiguous, precise language
- Use structured lists with clear categories

**MUST NOT:**
- Write as documentation about the AI for human readers
- Use third-person descriptions of AI behavior ("The AI should", "Copilot will", "The agent must", "Claude Code will")
- Mix instructions with commentary about the AI
- Use vague language ("try to", "consider", "maybe", "approximately", "around", "roughly")
- Use conditional language ("might", "could", "may") when giving instructions

---

## Literal Specification Compliance (from /src/claude/rules/literal-specification.md)

When you implement the topic bootstrap workflow:

**MUST:**
- Implement exactly the steps specified in this reference
- Create the directory structure as specified
- Use the bootstrap templates exactly as specified
- Follow the file naming conventions specified

**MUST NOT:**
- Add steps beyond those specified
- Modify the structure or naming conventions
- Add "helpful" enhancements or variations
- Anticipate additional bootstrap requirements

---

## Documentation-First Requirements (from /src/claude/rules/documentation-first.md)

When you establish conventions for topic structure:

**MUST:**
- Reference official documentation about knowledge base methodology when explaining bootstrap purpose
- Verify that directory structure and file naming align with documented practices
- State explicitly when establishing new conventions

**MUST NOT:**
- Assume bootstrap structure without documentation foundation
- Speculate about knowledge base organization conventions
- Implement practices without clear documented rationale

---

# Topic Bootstrap Workflow

## Purpose

The topic bootstrap workflow initializes a new research topic by creating its directory structure and templated files. This enables systematic research capture, operation logging, and organized fact collection for the new topic.

## Prerequisites

You must have:
- Topic slug (kebab-case identifier for the topic)
- Topic name (display-friendly topic title)
- Knowledge from first topic research session to populate initial index metadata
- Completion of workspace bootstrap (global `.memory/knowledge-base-index.md` exists)

## Bootstrap Steps

### Step 1: Create Topic Directory

Create the topic directory at workspace `.memory/` location:

```bash
mkdir -p ${WORKSPACE_ROOT}/.memory/[topic-slug]/
```

**Verify:** Check that the directory exists:

```bash
ls -la ${WORKSPACE_ROOT}/.memory/[topic-slug]/
```

### Step 2: Create Topic Index File

Create the `[topic-slug]-index.md` file using the topic index template.

**Source:** See [topic-index-template.md](topic-index-template.md) for the complete template structure and guidelines.

**MUST:**
- Use the template structure exactly as specified in topic-index-template.md
- Fill Knowledge Summary section with:
  - Overview (1-2 sentences describing research focus)
  - Research Domains (primary areas within topic)
  - Core Terminology (key concepts)
  - Verification Status (0 verified, 0 unverified, 0 disproven initially)
  - Total Findings (0 initially)
  - Last Updated (today's date in YYYY-MM-DD format)
- Initialize Fact Files section with planned fact file name
- Create empty Findings table with column headers but no rows (populate as findings are captured; Terms column will accumulate as terms are verified and linked)

**File location:** `${WORKSPACE_ROOT}/.memory/[topic-slug]/[topic-slug]-index.md`

### Step 3: Create Topic Log File

Create the `[topic-slug]-log.md` file using the topic log template.

**Source:** See [topic-log-template.md](topic-log-template.md) for the complete template structure and guidelines.

**MUST:**
- Use the template structure exactly as specified in topic-log-template.md
- Fill header with:
  - Topic: [topic-slug]
  - Session started: Today's date (YYYY-MM-DD format)
- Create initial bootstrap operation with ID `OP-YYYY-MM-DD-001` documenting:
  - Operation type: "Session initialization - topic bootstrap"
  - Files created: All three files created in this step
  - Key output: "Topic [topic-slug] directory and initial files created"
  - Timestamp: Today's date

**File location:** `${WORKSPACE_ROOT}/.memory/[topic-slug]/[topic-slug]-log.md`

### Step 4: Create Topic Facts File

Create the `[topic-slug]-facts.md` file using the topic facts template.

**Source:** See [topic-facts-template.md](topic-facts-template.md) for the complete template structure and guidelines.

**MUST:**
- Use the template structure exactly as specified in topic-facts-template.md
- Add file header with topic name: `# [Topic Name] - Fact File`
- Initialize as empty (no findings yet)
- Do NOT add any initial findings

**File location:** `${WORKSPACE_ROOT}/.memory/[topic-slug]/[topic-slug]-facts.md`

### Step 4a: Plan Subtopic Structure (Conditional)

If your topic will use semantic subtopics (organizational groupings for different research areas):

**MUST:**
- Identify the logical subtopics that will organize findings
- Document subtopic names for later use
- Each subtopic will create a subdirectory and facts files
- Subtopic naming convention: `[topic-slug]-[subtopic-name]` (kebab-case)

**Example for github-api topic:**
- `github-api-authentication` → credential management topics
- `github-api-comment-resolution` → PR comment workflow topics
- `github-api-integration` → integration patterns topics

**Do NOT create subtopic directories during bootstrap** - create them as subtopics emerge during research. Bootstrap step focuses on top-level topic structure only.

### Step 5: Verify Topic Bootstrap Completion

After creating all files:

**Verify:**
1. Directory exists: `${WORKSPACE_ROOT}/.memory/[topic-slug]/`
2. Index file exists: `${WORKSPACE_ROOT}/.memory/[topic-slug]/[topic-slug]-index.md` with all required sections
3. Log file exists: `${WORKSPACE_ROOT}/.memory/[topic-slug]/[topic-slug]-log.md` with bootstrap operation
4. Facts file exists: `${WORKSPACE_ROOT}/.memory/[topic-slug]/[topic-slug]-facts.md` with file header

If any file is missing or incomplete, halt and report the missing component.

### Step 6: Update Central Knowledge Base Index

After topic bootstrap completes, update the central knowledge base index.

**MUST:**
- Read `.memory/knowledge-base-index.md`
- Add new Topic Directory section matching the topic index's Knowledge Summary
- Add row to Central Index Maintenance Log with:
  - Date: Today (YYYY-MM-DD)
  - Topic: [topic-slug]
  - Action: "Topic directory created"
  - Details: "[topic-name] research initiated"

**Do NOT create new sections if not already done by main bootstrap.**

### Step 7: Create Terms Index File (Optional)

If your topic will use semantic term indexing:

Create `index-terms.md` in the topic directory following [term-indexing.md](term-indexing.md) guidelines.

**File location:** `${WORKSPACE_ROOT}/.memory/[topic-slug]/index-terms.md`

---

# Subtopic File Creation Requirements

## Hard Rule: Topic Column ↔ Subtopic Files

When findings are captured with a Topic value in the index:

**MANDATORY:**
- The Topic value MUST correspond to a subtopic that has an actual facts file
- Every Topic entry in the Findings table links to a real file at `[topic-slug]-[subtopic]/[topic-slug]-[subtopic]-facts.md`
- If a finding's Topic column says "Authentication", the file `github-api-authentication/github-api-authentication-facts.md` MUST exist
- Findings are extracted from the main facts file and placed into their subtopic-specific files
- The index Findings table links to the subtopic files, not the main facts file

**MUST NOT:**
- List a Topic value unless its subtopic file exists
- Link findings to non-existent files
- Keep findings in generic facts files if they belong to a labeled subtopic

## When to Create Subtopic Files

Create a subtopic file when:

1. **First finding for that topic area is captured** - Extract it immediately into a new subtopic file
2. **Topic value is assigned in index** - That Topic must have a corresponding facts file
3. **Moving findings from main facts file** - Create subtopic directory and facts files, then update index links

**Subtopic File Template:**

When creating `[topic-slug]-[subtopic]/[topic-slug]-[subtopic]-facts.md`:

```markdown
# [Topic Slug] [Subtopic Name] - Facts

## See Also
- [Disproven findings](github-api-[subtopic]-facts-disproven.md) (if applicable)

[Findings follow...]
```

Create disproven companion file if subtopic has disproven findings:
- File: `[topic-slug]-[subtopic]-facts-disproven.md` (same directory)
- Location: `.memory/[topic-slug]/[subtopic]/`
- Content: Disproven findings with evidence and rectifications

## Updating Index When Creating Subtopics

When you create subtopic files:

1. **Update main index Fact Files section** - Add entry in Subtopics subsection with link to subtopic facts file
2. **Update Findings table links** - Move finding links from main facts file to subtopic facts files
3. **Update Findings table Topic column** - Topic value determines which subtopic file finding links to
4. **Preserve Terms column** - Keep term links intact during migration

---

# Topic Bootstrap Invocation

When you invoke topic bootstrap:

1. Receive topic slug and topic name from user or research context
2. Verify workspace bootstrap is complete (check that `.memory/knowledge-base-index.md` exists)
3. Execute Steps 1–5 in sequence
4. Execute Step 6 to update central index
5. Optionally execute Step 7 for term indexing
6. Verify completion at each step
7. Report success with paths to created files

Do NOT proceed to research until all bootstrap steps complete.

---

# Topic Bootstrap Idempotency

Topic bootstrap MUST be idempotent:

- If topic directory already exists, do not recreate it
- If topic files already exist, do not overwrite them
- Report "Topic bootstrap complete: existing directory and files verified" rather than "created"

**Verify existing state:**

```bash
# Check if topic directory exists
if [ -d "${WORKSPACE_ROOT}/.memory/[topic-slug]" ]; then
  echo "Topic directory exists"
fi

# Check if all required files exist
for file in "[topic-slug]-index.md" "[topic-slug]-log.md" "[topic-slug]-facts.md"; do
  if [ -f "${WORKSPACE_ROOT}/.memory/[topic-slug]/$file" ]; then
    echo "$file exists"
  fi
done
```

---

# Topic Bootstrap Parameters

When invoking topic bootstrap, specify:

- **topic-slug** (required): Kebab-case identifier (e.g., `github-api`, `oauth-implementation`)
- **topic-name** (required): Display-friendly topic title (e.g., "GitHub API Research", "OAuth 2.0 Implementation")
- **research-domains** (optional): Comma-separated list of primary research domains
- **core-terminology** (optional): Comma-separated list of key concepts (can be populated later)

---
