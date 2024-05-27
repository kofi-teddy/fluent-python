from typing import List


def increasing_triplet(array: List[int]) -> bool:
    """
    Check if the array contains an increasing triplet.

    Args:
        array (List[int]): The array to check.

    Returns:
        bool: True if the array contains an increasing triplet, False otherwise.
    """
    lowest_price = array[0]
    middle_price = float('inf')

    for price in array:
        if price <= lowest_price:
            lowest_price = price
        elif price <= middle_price:
            middle_price = price
        else:
            return True

    return False