import os


def find_directories(directory: str) -> None:
    """
    Recursively finds and prints all directories within the given directory.

    Args:
        directory: The directory to search for subdirectories.

    Returns:
        None
    """
    for filename in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, filename)) and filename not in (".", ".."):
            print(os.path.join(directory, filename))
            # Recursively call this function on the subdirectory:
            find_directories(os.path.join(directory, filename))


print(find_directories("."))