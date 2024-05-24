from typing import List


def has_duplicate_value(array: List[int]) -> bool:
    """
    Check if an array has any duplicate values.

    Args:
        array: A list of integers.

    Returns:
        True if the array has duplicate values, False otherwise.
    """
    # Presort the array
    array.sort()

    # Iterate through the values in the array up until the last one
    for i in range(len(array) - 1):
        # If the value is identical to the next value in the array, we found a duplicate
        if array[i] == array[i + 1]:
            return True

    # If we get to the end of the array without finding any duplicates
    return False
