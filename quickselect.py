from typing import List

def quickselect(kth_lowest_value: int, left_index: int, right_index: int, array: List[int]) -> int:
    """
    Selects the kth lowest value from the given subarray using the Quickselect algorithm.

    Args:
        kth_lowest_value (int): The value to select.
        left_index (int): The left index of the subarray.
        right_index (int): The right index of the subarray.
        array (List[int]): The input array.

    Returns:
        int: The kth lowest value.

    Raises:
        IndexError: If the indices are out of range.

    """
    if right_index - left_index <= 0:
        return array[left_index]

    pivot_index = partition(left_index, right_index, array)

    if kth_lowest_value < pivot_index:
        return quickselect(kth_lowest_value, left_index, pivot_index - 1, array)
    elif kth_lowest_value > pivot_index:
        return quickselect(kth_lowest_value, pivot_index + 1, right_index, array)
    else:  # if kth_lowest_value == pivot_index
        return array[pivot_index]

def partition(left_index: int, right_index: int, array: List[int]) -> int:
    """
    Partitions the subarray around a pivot and returns the index of the pivot.

    Args:
        left_index (int): The left index of the subarray.
        right_index (int): The right index of the subarray.
        array (List[int]): The input array.

    Returns:
        int: The index of the pivot.

    Raises:
        IndexError: If the indices are out of range.

    """
    # Implementation of partition logic goes here
    pass