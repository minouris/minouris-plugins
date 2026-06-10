---
name: verify-analysis
description: Verify research findings or terms against authoritative sources with sub-agent autonomy
allowed-tools: Read, Edit, Write, WebFetch, WebSearch
context: fork
---

# Verify Analysis Skill

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
/verify-analysis fact <topic> [<subtopic>] <finding-id>
/verify-analysis term <topic> [<subtopic>] <term-id>
```

### Parameters

- **verification-type** (required): `fact` or `term`
- **topic** (required): Topic slug (e.g., `github-api`)
- **subtopic** (optional): Subtopic folder name (e.g., `github-api-authentication`)
- **id** (required): Finding ID (e.g., `FINDING-2026-03-11-06`) or Term ID/name (e.g., `TERM-2026-03-11-06` or `Pull Request`)

### Examples

```
/verify-analysis fact github-api FINDING-2026-03-11-06
/verify-analysis fact github-api github-api-authentication FINDING-2026-03-11-16
/verify-analysis term github-api TERM-2026-03-11-06
/verify-analysis term github-api github-api-actions TERM-2026-03-22-04
/verify-analysis term github-api "Pull Request"
```

---

## Verification Workflows

### Fact Verification

For detailed fact verification workflow, see [verify-fact-workflow.md](references/verify-fact-workflow.md).

Executes:
1. Locate finding in memory file
2. Fetch source and gather evidence
3. Determine verification status (VERIFIED/DISPROVEN/MANUAL)
4. Create verification working document with all proof text
5. Update fact file only after evidence is documented
6. Archive disproven findings to `-disproven.md`
7. Report results

### Term Verification

For detailed term verification workflow, see [verify-term-workflow.md](references/verify-term-workflow.md).

Executes:
1. Locate term in memory file
2. Fetch authoritative definition sources
3. Verify definition, scope, and consistency
4. Determine verification status (VERIFIED/DISPUTED/MANUAL)
5. Create verification working document with all proof text
6. Update term file only after evidence is documented
7. Archive disputed terms to `-disproven.md`
8. Report results

## Post-Verification Operations

After verification is complete, this skill performs all post-verification updates exclusively:

### For Verified Findings/Terms
- See [update-finding-tag.md](references/update-finding-tag.md) - Tag finding/term with verification status and link to verification document
- See [update-index.md](references/update-index.md) - Update analysis index to reflect newly verified item

### For Disproven/Disputed Items
- See [archive-disproven-finding.md](references/archive-disproven-finding.md) - Archive to `-disproven.md` with full disproof evidence

### Logging
- See [verification-logging.md](references/verification-logging.md) - Log verification operation to topic log

**CRITICAL:** The analysis skill MUST NOT perform any post-verification operations. All verification status updates, index updates, and archiving are the exclusive responsibility of verify-analysis.

---

## Integration with Workflows

### Fact Verification
Invoked by fact-capture.md inline verification workflow:
1. Fact is appended to memory file with `[NOT YET VERIFIED]` tag
2. `/verify-analysis fact` skill is invoked as background agent
3. Verification working document is created/updated with detailed verification entry
4. Fact file is updated with verification tag from working document
5. Index is updated with new verified fact
6. Verification result reported to calling context

### Term Verification
Invoked upon term creation:
1. Term is appended to memory file with `**Verified:** NOT YET VERIFIED` tag
2. `/verify-analysis term` skill is invoked as background agent
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
