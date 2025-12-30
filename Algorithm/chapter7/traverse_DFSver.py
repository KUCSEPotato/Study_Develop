from os import listdir
from os.path import isfile, join

def traverse_file_dir_dfs(path):
    for entry in sorted(listdir(path)):
        full_path = join(path, entry)
        if isfile(full_path):
            print(full_path)  # Print the file path, if you want to list file name, use entry of parameter for print
        else:
            traverse_file_dir_dfs(full_path)

def main():
    root_path = "../"  # Change this to the desired directory path
    traverse_file_dir_dfs(root_path)

if __name__ == "__main__":
    main()