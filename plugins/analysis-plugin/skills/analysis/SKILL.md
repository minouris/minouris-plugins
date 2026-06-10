---
name: analysis
description: Research and analysis workflow with systematic fact capture, verification, and knowledge base maintenance
allowed-tools: Read, Write, Edit, WebFetch, WebSearch
---

# Research/Analysis Skill

Perform systematic investigation and discovery, capturing research findings in a structured knowledge base. Extract semantic terms, verify facts against authoritative sources, and maintain indexed knowledge for use by other skills. Execute two distinct research workflows: procedural research (finding and testing procedures) and analytical research (examining artifacts and capturing findings).

## Overview

When you engage this skill, follow a rigorous research methodology:
- Documentation-first verification requirements
- Two-stage text search (keyword → direct examination)
- Systematic fact capture with clarifications
- Automatic semantic term extraction and linking
- Disproven finding archival (never delete)
- Fact verification for knowledge base integrity
- Operation logging for session continuity

## Documentation-First Principles

When you conduct research with this skill, operate under strict documentation-first principles. See [documentation-first.md](references/documentation-first.md) for complete requirements including:
- Mandatory official source verification
- Two-stage text search policy (keyword search → direct file examination)
- No speculation or assumptions
- Explicit uncertainty statements when sources unavailable

## Knowledge Base Bootstrap

When you engage this skill for the first time in a workspace, you must bootstrap the knowledge base structure that enables all subsequent research and fact collection.

See [bootstrap.md](references/bootstrap.md) for the bootstrap workflow, which:
- Creates the `.memory/` directory at the workspace root
- Initializes `knowledge-base-index.md` as the central discovery index
- Verifies structure before proceeding to research workflows

**Key principle:** Bootstrap is idempotent — running it again when the structure already exists verifies the structure and reports success without overwriting existing files.

## Topic Bootstrap

When you begin research on a new topic, you must bootstrap the topic structure that organizes findings, logs operations, and maintains topic-specific metadata.

See [topic-bootstrap.md](references/topic-bootstrap.md) for the topic bootstrap workflow, which:
- Creates the `[topic-slug]/` directory within `.memory/`
- Initializes `[topic-slug]-index.md` for organizing findings
- Initializes `[topic-slug]-log.md` for session continuity
- Initializes `[topic-slug]-facts.md` for fact capture
- Updates the central knowledge base index with the new topic

**Key principle:** Topic bootstrap is idempotent — running it again when the topic structure already exists verifies the structure and reports success without overwriting existing files.

**Topic Bootstrap Templates:**
- See [topic-index-template.md](references/topic-index-template.md) for index file structure
- See [topic-log-template.md](references/topic-log-template.md) for log file structure
- See [topic-facts-template.md](references/topic-facts-template.md) for facts file structure

## Research Workflows

### Workflow 1: Procedural Research

When you are asked to find, test, and verify a procedure or process, use this workflow. See [procedural-research.md](references/procedural-research.md) for:
- Web/documentation search procedures
- Test result documentation
- Iterative refinement based on testing
- Fact file capture format

### Workflow 2: Analytical Research

When you are asked to examine artifacts systematically and capture findings, use this workflow. See [analytical-research.md](references/analytical-research.md) for:
- Artifact indexing and systematic examination
- Fact capture and index maintenance
- Disproven finding archival
- Multi-file research organization

## Your Process

### CRITICAL: Memory File Location

When you create or update memory files during research, use this path structure ONLY:

```
.memory/[topic-slug]/[topic-slug]-facts.md
.memory/[topic-slug]/[topic-slug]-terms.md
.memory/[topic-slug]/[topic-slug]-index.md
```

**DO NOT create files in these wrong locations:**
- ❌ `src/claude/projects/...` (WRONG)
- ❌ `.claude/projects/.../memory/` (WRONG)
- ❌ Any location other than workspace root `.memory/` (WRONG)

All memory files must be in the workspace root `.memory/[topic-slug]/` directory.

### 1. Capture Research in Fact Files

See [fact-capture.md](references/fact-capture.md) for:
- Fact file naming conventions (`.memory/[topic]/[topic]-facts.md`, `.memory/[topic]/[topic]-[subtopic]/[topic]-[subtopic]-facts.md`)
- FINDING-YYYY-MM-DD-N format
- Clarifying existing facts (append with `Clarifies:` reference)
- When to create subtopic files
- **CRITICAL: Before finalizing a finding, verify it uses correct terminology:** Extract terms from the finding, invoke `/verify-analysis term` for each, amend finding to use verified term names/IDs

**Key principle:** During research phase, write ONLY to fact files. Use verified terminology in findings.

### 1.5. Extract and Maintain Semantic Terms

See [term-capture.md](references/term-capture.md) for:
- Term definition and fine-grained scoping
- Automatic term extraction from fact findings
- On-demand term extraction workflow
- Bidirectional linking between terms and facts
- Term validation against same criteria as facts
- Term archival and disproven tracking

See [term-indexing.md](references/term-indexing.md) for:
- Term entry template and standardized formatting
- Term index file organization and naming conventions
- Central index maintenance (`index-terms.md`)
- Term verification workflow and status tracking
- File size management (500-line limit per index file)

**Key principle:** When you extract terms, create hierarchical semantic indexing with standardized formatting. Extract terms automatically when facts introduce new concepts, maintain bidirectional links between facts and terms, and organize terms into properly formatted glossaries.

### 2. Archive Disproven Findings

See [disproven-archive.md](references/disproven-archive.md) for:
- Moving findings from fact file to `-disproven.md` companion
- Disproof metadata format
- Preservation rationale

**Key principle:** Never delete disproven findings. Archive immediately with full context.

**CRITICAL:** This refers to findings disproven DURING RESEARCH (user feedback that a finding is inaccurate). Findings disproven DURING VERIFICATION are archived by the verify-analysis skill, NOT the analysis skill.

### 3. Post-Verification Operations (verify-analysis Skill Only)

**CRITICAL:** The following operations are the EXCLUSIVE responsibility of the verify-analysis skill:
- Verify fact content against authoritative sources
- Update verification status tags on findings/terms
- Update indexes with newly verified findings/terms (findings added to findings index ONLY after verification)
- Archive findings/terms when validation fails
- Log verification operations

**MUST NOT:** The analysis skill performs any of these operations. Only verify-analysis handles all post-verification updates.

When fact verification is needed, invoke `/verify-analysis fact` and let that skill handle all verification, index updates, and logging.

### 4. Operation Logging
- Session initialization protocol (ask for topic slug, restore context)
- Significant operations requiring logging
- Log file format (`.memory/[topic]/[topic]-log.md`)

**Key principle:** Log after each significant operation to enable session continuity.

## Key Principles

### Processing Artifacts for Knowledge Base

**MUST:**
- Store all research artifacts in `.memory/` (fact files, indices, disproven archives, terms files)
- Capture research broadly in fact files; filter as research progresses when appropriate
- Extract semantic terms automatically from findings
- Verify extracted terms using `/verify-analysis term` before considering findings complete
- Amend findings to use verified terminology (term IDs or verified names)
- Maintain bidirectional links between facts and terms
- Archive findings to `-disproven.md` files immediately when the user disproves them
- Invoke `/verify-analysis fact` when verification of findings is needed; do not perform verification yourself

### Knowledge Base Maintenance

**MUST:**
- Archive disproven findings immediately to preserve history
- Maintain the analysis index for navigation and transparency
- Keep fact files and indexes in sync

### Transparency

**MUST:**
- Capture all research in fact files, including approaches attempted and dead ends
- Never delete disproven findings — archive them with the reason for disproof
- Include timestamps on all entries
- Maintain traceability from fact file entries to original sources

## Response to User

### On First Load (MANDATORY)

When you are invoked in a new session, before anything else:

1. Check if the knowledge base is bootstrapped: does `.memory/knowledge-base-index.md` exist?
2. If not bootstrapped, invoke `/analysis bootstrap` to initialize the knowledge base
3. Ask: "What topic are we working on? (This sets the session context — e.g., `ai-problems-analysis`)"
4. Once the user provides the topic slug, check if the topic directory exists at `.memory/[topic]/`
5. If topic directory does not exist, invoke `/analysis bootstrap-topic [topic-slug] [topic-name]` to create the topic
6. Once the topic directory exists, attempt to read `.memory/[topic]/[topic]-log.md`
7. If the log exists, summarise the last 1–3 entries to the user: operation type, files changed, and next step recorded
8. Confirm: "Session context loaded from `.memory/[topic]/[topic]-log.md`. Ready to continue."
9. If no log exists, confirm: "Topic `[topic]` initialized. Ready to begin research."

**MUST NOT:**
- Begin any research or respond to the first task before completing steps 1–9
- Assume a topic slug without asking
- Assume topic directory exists without checking

---

### When Engaged for Research

- For **procedural research**: See [procedural-research.md](references/procedural-research.md) for complete workflow
- For **analytical research**: See [analytical-research.md](references/analytical-research.md) for complete workflow

### Key Reminders

**MUST:**
- Bootstrap the knowledge base structure using `/analysis bootstrap` on first use in a workspace
- Bootstrap each topic using `/analysis bootstrap-topic [topic-slug] [topic-name]` before beginning research on that topic
- Store all processing artifacts in `.memory/` directory initialized by bootstrap
- Extract terms automatically from findings with singular scope
- Verify extracted terms using `/verify-analysis term` before considering findings complete
- Amend findings to use verified terminology from verified terms
- Maintain bidirectional links between facts and terms
- Capture broadly in fact files; archive disproven findings immediately, never delete
- Update terms index after each term operation
- **Maintain Knowledge Summary section in topic index** — ensure it reflects actual topic contents, update finding counts when verification occurs
- **Update central knowledge base index** at `.memory/knowledge-base-index.md` (create entry when first topic created; update only when scope changes). Use [bootstrap-template.md](references/bootstrap-template.md) as the structure reference.
- Run [record-operation](../../prompts/record-operation.prompt.md) with the topic slug after each significant operation (if available)
- Continue research without interruption for approval

**MUST NOT:**
- Bundle multiple concepts into a single term (each term = singular scope)
- Create terms without clear source citation
- Delete or lose bidirectional links between facts and terms

---

## Claude Code Tool Usage

This skill uses the following Claude Code tools:

- **Read**: Read fact files, source code, documentation
- **Write**: Create new fact files, indices
- **Edit**: Update existing fact files, indices, append entries
- **Grep**: Search code for patterns and keywords
- **Glob**: Find files matching patterns
- **Bash**: Execute tests, verify procedures, run commands
- **WebFetch**: Retrieve and analyse web documentation
- **WebSearch**: Find authoritative sources and official documentation

---

## Invocation

Invoke this skill when you need to:
- Bootstrap a knowledge base in a new workspace
- Bootstrap a new research topic
- Research and document a technical procedure
- Analyse a codebase or project systematically
- Capture research findings with proper citation and verification
- Build and maintain a structured knowledge base for a topic

**Workspace Bootstrap:**
```
/analysis bootstrap
```

Invokes the bootstrap workflow to initialize the `.memory/` directory and `knowledge-base-index.md`.

**Topic Bootstrap:**
```
/analysis bootstrap-topic [topic-slug] [topic-name]
```

Invokes the topic bootstrap workflow to create topic directory, index, log, and facts files. For example:
```
/analysis bootstrap-topic github-oauth "GitHub OAuth Implementation"
```

See [topic-bootstrap.md](references/topic-bootstrap.md) for the complete topic bootstrap workflow.

**Research Engagement:**
```
/analysis
```

Then specify whether you're conducting procedural or analytical research, and provide the scope.
