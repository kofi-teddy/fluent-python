
from typing import List


def two_sum_10(array: List[int]) -> bool:
    """
    Finds the sum of the first two numbers in the array that add up to 10.

    Args:
        array (List[int]): A list of numbers.

    Returns:
        int: The sum of the first two numbers in the array that add up to 10.
    """
    for i, iVal in enumerate(array):
        for j, jVal in enumerate(array):
            if i != j and iVal + jVal == 10:
                # return iVal + jVal
                return True
    return False