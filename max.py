from typing import List

# def find_max(array: List[int]) -> int:
#     """
#     Finds the maximum number in the given array.

#     Args:
#         array: A list of integers.

#     Returns:
#         The maximum number in the array.
#     """
#     greatest_number_so_far = array[0]
#     for i in range(len(array)):
#         if array[i] > greatest_number_so_far:
#             greatest_number_so_far = array[i]
#     return greatest_number_so_far


# def find_max(array: List[int]) -> int:
#     """
#     O(N^2)
#     Finds the maximum number in the given array.

#     Args:
#         array: A list of integers.

#     Returns:
#         The maximum number in the array.
#     """
#     greatest_number_so_far: int = array[0]
#     for i in range(len(array)):
#         if array[i] > greatest_number_so_far:
#             greatest_number_so_far = array[i]
#     return greatest_number_so_far


def find_max(array: List[int]) -> int:
    """
    O(N log N)
    Finds the maximum number in the given array.

    Args:
        array: A list of integers.

    Returns:
        The maximum number in the array.
    """
    array.sort()
    return array[-1]
