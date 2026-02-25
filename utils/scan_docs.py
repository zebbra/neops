import os

DOCS_DIR = "/home/leandro/projects/neops/docs"

def scan_file(filepath):
    issues = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        return [f"Could not read file: {e}"]
    
    in_code_block = False
    code_block_lang = ""
    code_block_content = []
    code_block_start_line = 0
    
    for i, line in enumerate(lines):
        line_num = i + 1
        
        # Check for bad links: ../
        if "(../" in line:
            issues.append(f"Line {line_num}: Possible issue (verify with AGENTS.md): Link references parent directory (../)")

        # Check for code blocks
        if line.strip().startswith("```"):
            if in_code_block:
                # End of code block
                content_str = "".join(code_block_content).strip()
                # Ignore mermaid
                if code_block_lang != "mermaid":
                    # Check if it is a snippet include
                    is_snippet = "--8<--" in content_str
                    if not is_snippet:
                        # Check length
                        if len(code_block_content) > 5:
                             issues.append(f"Line {code_block_start_line}: Possible issue (verify with AGENTS.md): Inline code block > 5 lines (lang: {code_block_lang}). Should be external.")
                
                in_code_block = False
                code_block_content = []
                code_block_lang = ""
            else:
                # Start of code block
                in_code_block = True
                code_block_lang = line.strip().lstrip("`").strip()
                code_block_start_line = line_num
        
        elif in_code_block:
             code_block_content.append(line)

    return issues

def main():
    print(f"Scanning {DOCS_DIR}...", flush=True)
    all_issues = {}
    for root, dirs, files in os.walk(DOCS_DIR):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, DOCS_DIR)
                file_issues = scan_file(full_path)
                if file_issues:
                    all_issues[rel_path] = file_issues

    if not all_issues:
        print("No issues found!", flush=True)
    else:
        print(f"Found issues in {len(all_issues)} files.", flush=True)
        for f, issues in all_issues.items():
            print(f"\nFile: {f}", flush=True)
            for issue in issues:
                print(f"  - {issue}", flush=True)

if __name__ == "__main__":
    main()
