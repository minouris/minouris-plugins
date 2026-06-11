import re
import sys
import argparse

def insert_new_problem(file_path, category, prob_id, summary, description):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Normalize the ID formatting just in case (e.g., ensuring "PROB-005")
    prob_id = prob_id.upper()
    if not prob_id.startswith("PROB-"):
        prob_id = f"PROB-{prob_id}"

    # Define the exact strings to insert
    new_table_row = f"| <a name=\"{prob_id}\"></a>[{prob_id}](#details-{prob_id}) | {summary} |\n"
    
    new_detail_block = (
        f"\n**<a name=\"details-{prob_id}\"></a>[{prob_id}](#{prob_id}): {summary}**\n\n"
        f"{description}\n"
    )

    # Locate the target category section block
    # Matches "### Category Name" up to the next "### " header or End of File
    category_regex = rf"(### {re.escape(category)}\n.*?(?=\n### |$))"
    category_match = re.search(category_regex, content, re.DOTALL)
    
    if not category_match:
        print(f"Error: Category '{category}' not found in the file.", file=sys.stderr)
        sys.exit(1)
        
    category_block = category_match.group(1)

    # --- STEP 1: Insert the row into the Summary Table ---
    # Find the last table row inside this category block
    table_row_regex = r"(\|.*?\|.*?\|\n)"
    table_rows = list(re.finditer(table_row_regex, category_block))
    
    if not table_rows:
        print(f"Error: Could not locate the summary table under '{category}'.", file=sys.stderr)
        sys.exit(1)
        
    last_row = table_rows[-1]
    # Insert our new row right after the last table row found
    updated_category_block = (
        category_block[:last_row.end()] + 
        new_table_row + 
        category_block[last_row.end():]
    )

    # --- STEP 2: Insert the Long Description block ---
    # Find the last detail paragraph currently in this category
    detail_regex = r"(\*\*<a name=\"details-PROB-\d+\">.*?)(?=\n\*\*<a name=\"details-PROB-|\n### |$)"
    details = list(re.finditer(detail_regex, updated_category_block, re.DOTALL))
    
    if details:
        # If detail blocks already exist, append ours right after the last one
        last_detail = details[-1]
        updated_category_block = (
            updated_category_block[:last_detail.end()] + "\n" +
            new_detail_block + 
            updated_category_block[last_detail.end():]
        )
    else:
        # Fallback: If no detail blocks exist yet, append it to the very end of the category block
        updated_category_block = updated_category_block.rstrip() + "\n" + new_detail_block

    # --- STEP 3: Write changes back to file ---
    # Replace the old category block with our completely updated one
    final_content = content.replace(category_block, updated_category_block)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
        
    print(f"Successfully added {prob_id} to '{category}' section!")

if __name__ == "__main__":
    # Setting up the argument parser for CLI execution
    parser = argparse.ArgumentParser(description="Insert a new problem row and description into Markdown architecture.")
    parser.add_argument("--file", default="file.md", help="Path to the markdown file")
    parser.add_argument("category", help="Category heading name (e.g., 'General')")
    parser.add_argument("id", help="Problem ID number or string (e.g., '005' or 'PROB-005')")
    parser.add_argument("summary", help="Brief summary for the table row and header")
    parser.add_argument("description", help="The long-form description paragraphs")

    args = parser.parse_regex = parser.parse_args()
    
    insert_new_problem(args.file, args.category, args.id, args.summary, args.description)