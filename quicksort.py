from typing import List


def quicksort(left_index: int, right_index: int) -> None:
    """
    Sorts a subarray using the quicksort algorithm.

    Args:
        left_index (int): The left index of the subarray.
        right_index (int): The right index of the subarray.

    Returns:
        None
    """
    # Base case: the subarray has 0 or 1 elements
    if right_index - left_index <= 0:
        return

    # Partition the range of elements and grab the index of the pivot
    pivot_index = partition(left_index, right_index)

    # Recursively call this quicksort method on the left side of the pivot
    quicksort(left_index, pivot_index - 1)

    # Recursively call this quicksort method on the right side of the pivot
    quicksort(pivot_index + 1, right_index)

def partition(left_index: int, right_index: int) -> int:
    """
    Partitions a subarray and returns the index of the pivot.

    Args:
        left_index (int): The left index of the subarray.
        right_index (int): The right index of the subarray.

    Returns:
        int: The index of the pivot.
    """
    # Implementation of partitioning logic goes here
    # ...

    return pivot_index