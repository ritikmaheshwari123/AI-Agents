## Create a new directory and navigate into it

import os
# Define the new directory name
new_directory = "example_dir"
# Create the new directory
os.mkdir(new_directory)

item = os.listdir('.')
print(item)

## Joining paths

dir_name = "folder"
file_name = "file.txt"

full_path = os.path.join(dir_name, file_name)
print(full_path)  # Output: folder/file.txt (or folder\file.txt on Windows)

full_path = os.path.join(os.getcwd(),dir_name, file_name)
print(full_path)  # Output: /current/working/directory/folder/file.txt

### check if a path exists
path_exists = os.path.exists(full_path)
print(f"Path exists: {path_exists}")

## Check if it's a file or directory
is_file = os.path.isfile(full_path)
is_directory = os.path.isdir(full_path)
print(f"Is file: {is_file}")
print(f"Is directory: {is_directory}")

## Get absolute path
absolute_path = os.path.abspath(full_path)
print(f"Absolute path: {absolute_path}")


