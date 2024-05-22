from typing import List


def largest_product(array: List[int]) -> int:
    """
    Finds the largest product of three integers in the given array.

    Args:
        array: A list of integers.

    Returns:
        The largest product of three integers in the array.
    """
    largest_product_so_far = array[0] * array[1] * array[2]
    i = 0
    while i < len(array):
        j = i + 1
        while j < len(array):
            k = j + 1
            while k < len(array):
                if array[i] * array[j] * array[k] > largest_product_so_far:
                    largest_product_so_far = array[i] * array[j] * array[k]
                k += 1
            j += 1
        i += 1
    return largest_product_so_far