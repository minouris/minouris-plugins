# Update Finding with Verification Tag

**This file is loaded when: You need to tag a verified finding in the memory file.**

---

# Embedded Rules

## Literal Specification Compliance (from /src/claude/rules/literal-specification.md)

**Verification Tag Format is Expressly Specified - Compliance is MANDATORY:**

**MUST:**
- Use the exact tag format: `**Verified:** [VERIFIED on YYYY-MM-DD by {source-url}] ([details]({verification-file}#{finding-anchor}))`
- Include all required components: date, source URL, verification document path, anchor link
- Preserve exact markdown formatting and punctuation
- Use the specified date format (YYYY-MM-DD)

**MUST NOT:**
- Add fields to tag format beyond specification
- Modify tag format for convenience
- Change the structure or punctuation
- Skip any required component

---

## Execution

After verification is complete and documented in the verification working document, update the original finding in the fact file by adding the verification tag.

**DO NOT rewrite the entire file yet** - only tag this specific finding.

---

## Verification Tag Format

Add immediately after the finding content:

```markdown
**Verified:** [VERIFIED on YYYY-MM-DD by {source-url}] ([details]({verification-file}#{finding-anchor}))
```

### Tag Components

- `YYYY-MM-DD` - Date verification was completed
- `{source-url}` - Primary authoritative URL or `research synthesis` for multi-source findings
- `{verification-file}` - Path to verification document
- `{finding-anchor}` - Anchor link to verification section in document (lowercase with hyphens)

---

## Requirements

**MUST:**
- Include link to verification document in the verification tag
- Use the primary authoritative URL that verified this fact
- Use lowercase with hyphens for anchor links
- Preserve all other finding content unchanged
- Only tag if verification status is VERIFIED (not DISPROVEN or MANUAL)

**MUST NOT:**
- Rewrite the entire fact file (wait for finalization step)
- Remove or modify existing verification tags on other findings
- Omit the link to the verification document

---

## Output

Tracks the verification tag to be added to the finding, which will be applied during the finalization step when all post-verification operations are complete.
