from os import listdir
from os.path import isfile, join
from collections import deque

def traverse_file_dir(path):
    """
    Traverse a directory and return a list of all files within it and its subdirectories.

    Args:
        path (str): The root directory path to start the traversal.
    Returns:
        list: A list of file paths.
    """
    files = []
    queue = deque([path])

    while queue:
        current_path = queue.popleft()
        try:
            for entry in listdir(current_path):
                full_path = join(current_path, entry)
                if isfile(full_path):
                    files.append(full_path)
                else:
                    queue.append(full_path)
        except PermissionError:
            # Skip directories for which we don't have permission
            raise PermissionError(f"Permission denied: '{current_path}'")

    return files

def main():
    root_path = "../"  # Change this to the desired directory path
    all_files = traverse_file_dir(root_path)
    for file in all_files:
        print(file)

if __name__ == "__main__":
    main()