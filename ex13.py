# Working with file system

from pathlib import Path

# check current directory
cwd = Path.cwd()
print(cwd)

# combine file path and file name
# new_file = Path.joinpath(cwd, "new_file.text")
# print(new_file)

# Check if file exist
# print(new_file.exists())

# Get the parent directory
# parent = cwd.parent

# check for dir
# print(parent.is_dir())

# check for file
# print(parent.is_file())

# List file directories
# for child in parent.iterdir():
#     if child.is_dir():
#         print(child)

# Working with files
demo_file = Path(Path.joinpath(cwd, "demo.txt"))

# Get file name
print(demo_file.name)

# Get file extension
print(demo_file.suffix)

# Get the folder
print(demo_file.parent.name)

# Get the size
# print(demo_file.stat().st_size())

