from typing import List, Optional


def find_missing_number(array: List[int]) -> Optional[int]:
    """
    Finds the missing number in a sorted array of integers.

    Args:
        array: A list of integers.

    Returns:
        The missing number in the array, or None if no number is missing.
    """
    array.sort()
    for i in range(len(array)):
        if array[i] != i:
            return i
    return None