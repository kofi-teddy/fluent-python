from typing import List

def greatest_product_of_3(array: List[int]) -> int:
    """
    Returns the greatest product of three integers in the given array.

    Args:
        array: A list of integers.

    Returns:
        The greatest product of three integers in the array.

    Raises:
        ValueError: If the array has less than 3 elements.
    """
    if len(array) < 3:
        raise ValueError("Array must have at least 3 elements")

    array.sort()
    return array[-1] * array[-2] * array[-3]