from typing import List


def is_subset(array_1: List[int], array_2: List[int]) -> bool:
    """
    Checks if array_2 is a subset of array_1.

    Args:
        array_1: A list of integers.
        array_2: A list of integers.

    Returns:
        True if array_2 is a subset of array_1, False otherwise.
    """
    if len(array_1) > len(array_2):
        largest_array = array_1
        smallest_array = array_2
    else:
        largest_array = array_2
        smallest_array = array_1

    hash_table = {}
    for i in largest_array:
        hash_table[i] = True
    
    for i in smallest_array:
        if not hash_table[i]:
            return False
    return True