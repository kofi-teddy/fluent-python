from typing import List


def two_sum(array: List[int]) -> bool:
    """
    Check if there are two numbers in the array that add up to 10.

    Args:
        array (List[int]): The array to check.

    Returns:
        bool: True if there are two numbers that add up to 10, False otherwise.
    """
    hash_table = {}

    for i in range(len(array)):
        if hash_table.get(10 - array[i]):
            return True

        hash_table[array[i]] = True

    return False