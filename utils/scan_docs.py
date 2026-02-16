import os
import re

DOCS_DIR = "/home/leandro/projects/neops/docs"
ROOT_DIR = "/home/leandro/projects/neops"

def scan_file(filepath):
    issues = []
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    in_code_block = False
    code_block_lang = ""
    code_block_content = []
    
    for i, line in enumerate(lines):
        line_num = i + 1
        
        # Check for bad links: ../
        # Regex for [text](link) and ![alt](link)
        # We look for (../
        if "(../" in line:
            issues.append(f"Line {line_num}: Link references parent directory (../)")

        # Check for code blocks
        if line.strip().startswith("```"):
            if in_code_block:
                # End of code block
                # Analyze content
                content_str = "".join(code_block_content).strip()
                is_ignored_lang = code_block_lang in ["mermaid", "text", "sh", "bash", "console"] 
                # "text", "sh", "bash" might be allowed for simple things? 
                # Rule: "Code snippets should always be referenced from real code... Do never write code examples inlined"
                # This suggests language specific code (python, yaml, json, etc) should be external.
                # I will flag EVERYTHING that is non-mermaid and has content that is NOT a snippet include.
                
                is_snippet = "--8<--" in content_str
                
                if not is_ignored_lang and content_str and not is_snippet:
                     if code_block_lang not in ["mermaid"]:
                        # We might want to be strict.
                        if len(content_str.splitlines()) > 1: # multi-line code
                             issues.append(f"Line {line_num-len(code_block_content)-1}: Inlined code block (lang: {code_block_lang}) found. Should be external.")
                
                in_code_block = False
                code_block_content = []
                code_block_lang = ""
            else:
                # Start of code block
                in_code_block = True
                code_block_lang = line.strip().lstrip("`").strip()
        
        elif in_code_block:
             code_block_content.append(line)

    return issues

def main():
    print(f"Scanning {DOCS_DIR}...")
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
        print("No issues found!")
    else:
        print(f"Found issues in {len(all_issues)} files.")
        for f, issues in all_issues.items():
            print(f"\nFile: {f}")
            for issue in issues:
                print(f"  - {issue}")

if __name__ == "__main__":
    main()
