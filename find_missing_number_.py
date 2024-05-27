from typing import List


def find_missing_number(array: List[int]) -> int:
    """
    Find the missing number in an array.

    Args:
        array (List[int]): The array to check.

    Returns:
        int: The missing number.
    """
    full_sum = 0
    for i in range(1, len(array) + 1):
        full_sum += i

    current_sum = 0
    for num in array:
        current_sum += num

    return full_sum - current_sum