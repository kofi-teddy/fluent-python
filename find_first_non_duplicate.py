def find_first_non_duplicate(text: str) -> str:
    """
    Finds the first non-duplicate in the array.

    Args:
        array (List[str]): A list of strings.

    Returns:
        str: The first non-duplicate in the array.
    """
    hash_table = {}
    for i in text:
        if hash_table.get(i):
            hash_table[i] += 1
        else:
            hash_table[i] = 1

    for key, value in hash_table.items():
        if value == 1:
            return key
    return None


text = "minimum"
print(find_first_non_duplicate(text))