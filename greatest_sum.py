from typing import List


def max_sum(array: List[int]) -> int:
    """
    Find the maximum sum of any contiguous subarray.

    Args:
        array (List[int]): The array to find the maximum sum in.

    Returns:
        int: The maximum sum of any contiguous subarray.
    """
    current_sum = 0
    greatest_sum = 0

    for num in array:
        if current_sum + num < 0:
            current_sum = 0
        else:
            current_sum += num
            greatest_sum = max(greatest_sum, current_sum)

    return greatest_sum