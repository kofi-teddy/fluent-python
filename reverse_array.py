from typing import List


def reverse(array: List[int]) -> List[int]:
    """
    Reverse the order of elements in the array.

    Args:
        array (List[int]): The array to reverse.

    Returns:
        List[int]: The reversed array.
    """
    for i in range(len(array) // 2):
        array[i], array[len(array) - 1 - i] = array[len(array) - 1 - i], array[i]

    return array