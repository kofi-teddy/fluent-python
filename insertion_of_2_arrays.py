from typing import List


def intersection(first_array: List[int], second_array: List[int]) -> List[int]:
    """
    Finds the intersection of two arrays.

    Args:
        first_array (List[int]): The first array.
        second_array (List[int]): The second array.

    Returns:
        List[int]: The intersection of the two arrays.
    """
    result = []
    for i in range(len(first_array)):
        for j in range(len(second_array)):
            if first_array[i] == second_array[j]:
                result.append(first_array[i])
                break
    return result
