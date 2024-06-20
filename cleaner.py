import os
import sys

# List of common directories to clean
CLEANUP_DIRS = [
    os.path.join(os.getenv('TEMP')),  # Temp folder
    os.path.join(os.getenv('USERPROFILE'), 'Downloads'),  # Downloads folder
    os.path.join(os.getenv('USERPROFILE'), 'Documents'),  # Documents folder
]

# List of common file types to clean
CLEANUP_EXTENSIONS = ['.tmp', '.log', '.bak', '.old', '.chk', '.dmp']

def find_files_to_delete(directory, extensions):
    files_to_delete = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                files_to_delete.append(os.path.join(root, file))
    return files_to_delete

def main():
    all_files_to_delete = []
    for directory in CLEANUP_DIRS:
        if os.path.exists(directory):
            files_to_delete = find_files_to_delete(directory, CLEANUP_EXTENSIONS)
            all_files_to_delete.extend(files_to_delete)

    if not all_files_to_delete:
        print("No files to delete.")
        return

    print("Found the following files:")
    for file in all_files_to_delete:
        print(file)

    confirmation = input("Do you want to delete these files? (yes/no): ").strip().lower()
    if confirmation == 'yes':
        for file in all_files_to_delete:
            try:
                os.remove(file)
                print(f"Deleted: {file}")
            except Exception as e:
                print(f"Failed to delete {file}: {e}")
    else:
        print("No files were deleted.")

if __name__ == '__main__':
    main()
