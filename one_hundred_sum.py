from typing import List


def one_hundred_sum(array: List[int]) -> bool:
    """
    Checks if there are two numbers in the given array that sum up to 100.

    Args:
        array: A list of integers.

    Returns:
        True if there are two numbers in the array that sum up to 100, False otherwise.
    """
    left_index: int = 0
    right_index: int = len(array) - 1
    
    while left_index < len(array) // 2:
        if array[left_index] + array[right_index] != 100:
            return False
        left_index += 1
        right_index -= 1
    
    return True