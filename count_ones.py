from typing import List


def count_ones(outer_array: List[List[int]]) -> int:
    """
    Counts the number of 1s in the given 2D array.

    Args:
        outer_array (List[List[int]]): A 2D list of integers.

    Returns:
        int: The number of 1s in the 2D array.
    """
    count = 0
    for inner_array in outer_array:
        for element in inner_array:
            if element == 1:
                count += 1
    return count


outer_array = [
  [0, 1, 1, 1, 0],
  [0, 1, 0, 1, 0, 1],
  [1, 0]
]

print(count_ones(outer_array))