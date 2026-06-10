# Knowledge Base Bootstrap Feature

**This reference file provides the bootstrap workflow for initializing a new knowledge base instance in the workspace `.memory` directory.**

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

When you implement the bootstrap workflow:

**MUST:**
- Implement exactly the steps specified in this reference
- Create the directory structure as specified
- Use the bootstrap template exactly as specified
- Follow the file naming conventions specified

**MUST NOT:**
- Add steps beyond those specified
- Modify the structure or naming conventions
- Add "helpful" enhancements or variations
- Anticipate additional bootstrap requirements

---

## Documentation-First Requirements (from /src/claude/rules/documentation-first.md)

When you establish conventions for the knowledge base structure:

**MUST:**
- Reference official documentation about knowledge base methodology when explaining bootstrap purpose
- Verify that directory structure and file naming align with documented practices
- State explicitly when establishing new conventions

**MUST NOT:**
- Assume bootstrap structure without documentation foundation
- Speculate about knowledge base organization conventions
- Implement practices without clear documented rationale

---

# Bootstrap Workflow

## Purpose

The bootstrap workflow initializes a new knowledge base instance by creating the required directory structure and top-level index file. This enables the workspace to support multi-topic research and fact collection with organized, discoverable knowledge.

## Prerequisite

You must have the workspace root identified. Bootstrap creates the `.memory` directory as a sibling to the workspace root's existing directories (src/, docs/, etc.).

## Bootstrap Steps

### Step 1: Create `.memory` Directory

Create the `.memory` directory at the workspace root if it does not already exist:

```bash
mkdir -p ${WORKSPACE_ROOT}/.memory
```

**Verify:** Check that the directory exists:

```bash
ls -la ${WORKSPACE_ROOT}/.memory
```

### Step 2: Create Initial `knowledge-base-index.md`

Create the `knowledge-base-index.md` file at `${WORKSPACE_ROOT}/.memory/knowledge-base-index.md` using the bootstrap template.

**Source:** See [bootstrap-template.md](bootstrap-template.md) for the complete template structure and guidelines.

**MUST:**
- Use the template structure exactly as specified in bootstrap-template.md
- Set **Last Updated** to today's date (YYYY-MM-DD format)
- Initialize Quick Search Guide with at least one example topic mapping
- Initialize Topic Directories with at least one topic section following the template
- Create initial Maintenance Log entry with bootstrap date and "knowledge-base-index.md created"

**Example entry:**
```markdown
| 2026-03-23 | All | knowledge-base-index.md created | Initial knowledge base bootstrap |
```

### Step 3: Verify Bootstrap Completion

After creating both the directory and `knowledge-base-index.md`:

**Verify:**
1. Directory exists: `${WORKSPACE_ROOT}/.memory/` (contains at least `knowledge-base-index.md`)
2. Index file exists: `${WORKSPACE_ROOT}/.memory/knowledge-base-index.md`)
3. Index file contains all required sections from bootstrap template:
   - H1 "Knowledge Base Index"
   - **Last Updated** date
   - ## Quick Search Guide section with table
   - ## Topic Directories section with at least one topic
   - ## Central Index Maintenance Log section
   - ## Updating This Index section

If any verification fails, halt and report the missing component.

### Step 4: Add Topic Directories (Per Verified Topic)

When you begin research on a new topic and the topic is verified:

**Create topic directory:**
```bash
mkdir -p ${WORKSPACE_ROOT}/.memory/[topic-slug]/
```

**MUST:**
- Use kebab-case for topic slug (lowercase, hyphens)
- Create topic index file: `${WORKSPACE_ROOT}/.memory/[topic-slug]/[topic-slug]-index.md`
- Create topic facts file: `${WORKSPACE_ROOT}/.memory/[topic-slug]/[topic-slug]-facts.md`

See [index-maintenance.md](index-maintenance.md) for topic index file structure.
See [fact-capture.md](fact-capture.md) for topic facts file structure.

**Update `knowledge-base-index.md`:**
- Add new topic section under ## Topic Directories
- Follow the topic section template exactly (Knowledge Summary, Quick Links, Research Areas, Key Concepts)
- Update ## Central Index Maintenance Log with new entry: `| YYYY-MM-DD | [topic-slug] | Topic directory created | [topic-name] research initiated |`

---

# Bootstrap Invocation

When you invoke bootstrap:

1. Receive workspace root path from user or environment
2. Execute Steps 1–3 in sequence
3. Verify completion at each step
4. Report success with path to `knowledge-base-index.md`

Do NOT proceed to Step 4 until user explicitly requests research on a new topic.

---

# Bootstrap Idempotency

Bootstrap MUST be idempotent:

- If `.memory` directory already exists, do not recreate it
- If `knowledge-base-index.md` already exists, do not overwrite it
- Report "Bootstrap complete: existing directories and files verified" rather than "created"

**Verify existing state:**

```bash
# Check if .memory exists
if [ -d "${WORKSPACE_ROOT}/.memory" ]; then
  echo ".memory directory exists"
fi

# Check if knowledge-base-index.md exists
if [ -f "${WORKSPACE_ROOT}/.memory/knowledge-base-index.md" ]; then
  echo "knowledge-base-index.md exists"
fi
```

---
