---
name: add-problem
description: Adds a problem item to a given page's 'Problems' section. Use when asked to "Add a problem to..."
allowed-tools: AskUserQuestion, Edit, Write, Bash
---

Assign $ARGUMENTS[0] to PROBLEM_DOCUMENT
Assign $ARGUMENTS[1] to DESCRIPTION
Assign $ARGUMENTS[2] to CATEGORY (Optional)

1. Check to see if $PROBLEM_DOCUMENT exists

  **If it DOES NOT exist:**

  Use `AskUserQuestion` to query the user for a title for the document, and store it as $TITLE.

  Create $PROBLEM_DOCUMENT with the following content:

  ```markdown
  # $TITLE

  ```

2. Check to see if $PROBLEM_DOCUMENT has a `## Problems` heading

  **If it DOES NOT:**

  Insert a `## Problems` heading into the document.

3. If CATEGORY NOT has been assigned:

  Set CATEGORY = 'General'

4. Check to see if there is a `### $CATEGORY` heading under `## Problems`

  **If there IS NOT:**

  Append a `### $CATEGORY` heading beneath `## Problems`. If $CATEGORY = "General" it should be the FIRST Category after the `## Problems` heading.

  Treat the `### $CATEGORY` section of the document as the CURRENT_SECTION.

5. Check to see if the CURRENT_SECTION contains a table matching the contents of `templates/problem-table-template.md`

  **If it DOES NOT:**

  Append the contents of `templates/problem-table-template.md` to the CURRENT_SECTION.

6. Set PROB_ID = 
  ```!
  LAST_ID = $(grep -Po 'PROB-\d+' $PROBLEM_DOCUMENT 2> /dev/null | sort -V | tail -n -1 | cut -d'-' -f2)

  if [ -z $LAST_ID ]; then
    LAST_ID=0
  fi

  NEXT_ID=$(printf "%03d" $((10#$LAST_ID + 1)))

  echo "PROB-$NEXT_ID"
  ```

7. Query the user for a detailed description of the problem:

   **MUST:**
   - Identify all distinct claims or issues stated in the summary (DESCRIPTION)
   - For each claim, ask specific questions to understand:
     - Root cause (why does this happen?)
     - Impact (what breaks or fails?)
     - Current state vs. expected state
     - Affected workflows or tools
   - Continue asking follow-up questions until each claim in the summary has been fully explored
   - Ask the user to confirm when they have no additional information to provide

   **MUST NOT:**
   - Accept vague or incomplete answers without follow-up
   - Skip exploring any component mentioned in the summary
   - Stop questioning before all aspects of the summary are detailed

   Store their complete answer as DETAILED_DESCRIPTION.

8. Set RESULT = `python3 ${CLAUDE_SKILL_DIR}/scripts/add_problem.py --file $PROBLEM_DOCUMENT "$CATEGORY" "$PROBLEM_ID" "$DESCRIPTION" "$DETAILED_DESCRIPTION"`

10. If $Result = "Successfully added $PROB_ID$ to #CATEGORY section!" then report to the user that the problem was successfully added. Otherwise, report that there was an error.
