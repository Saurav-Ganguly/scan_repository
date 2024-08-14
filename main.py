import os

def write_tree_structure(output_file, path, prefix=''):
    entries = sorted(os.listdir(path))
    for i, entry in enumerate(entries):
        is_last = (i == len(entries) - 1)
        full_path = os.path.join(path, entry)
        
        if os.path.isdir(full_path):
            output_file.write(f"{prefix}{'└── ' if is_last else '├── '}{entry}/\n")
            write_tree_structure(output_file, full_path, prefix + ('    ' if is_last else '│   '))
        else:
            output_file.write(f"{prefix}{'└── ' if is_last else '├── '}{entry}\n")

def write_file_contents(output_file, path):
    with open(path, 'r', encoding='utf-8') as file:
        output_file.write(f"\n\n{'=' * 80}\n")
        output_file.write(f"File: {path}\n")
        output_file.write(f"{'=' * 80}\n\n")
        output_file.write(file.read())
        output_file.write("\n")

def scan_repository(root_path):
    output_file_path = os.path.join(root_path, 'feed_all_my_code_to_llm.txt')
    
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write("Repository Structure:\n\n")
        write_tree_structure(output_file, root_path)
        
        output_file.write("\n\nFile Contents:\n")
        for root, dirs, files in os.walk(root_path):
            for file in files:
                if file != 'feed_all_my_code_to_llm.txt' and file != os.path.basename(__file__):
                    file_path = os.path.join(root, file)
                    try:
                        write_file_contents(output_file, file_path)
                    except Exception as e:
                        output_file.write(f"\n\nError reading file {file_path}: {str(e)}\n")

if __name__ == "__main__":
    root_directory = os.path.dirname(os.path.abspath(__file__))
    scan_repository(root_directory)
    print(f"Repository scan complete. Output written to 'feed_all_my_code_to_llm.txt'")