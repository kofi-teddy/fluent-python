from typing import List


def find_first_duplicate(array: List[str]) -> str:
    """
    Finds the first duplicate in the array.

    Args:
        array (List[str]): A list of strings.

    Returns:
        str: The first duplicate in the array.
    """
    hash_table = {}
    for i in range(len(array)):
        if hash_table.get(array[i]):
            return array[i]
        hash_table[array[i]] = True
    return None 


print(find_first_duplicate(["a", "b", "c", "d", "c", "e", "f"]))