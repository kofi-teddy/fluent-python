from typing import List


def selectionSort(array: List[int]) -> List[int]:
    """
    Sorts the given array in ascending order using the selection sort algorithm.

    Parameters:
    array (List[int]): The array to be sorted.

    Returns:
    List[int]: The sorted array.
    """
    for i in range(len(array) - 1):
        lowestNumberIndex = i
        for j in range(i + 1, len(array)):
            if array[j] < array[lowestNumberIndex]:
                lowestNumberIndex = j
        if lowestNumberIndex != i:
            temp = array[i]
            array[i] = array[lowestNumberIndex]
            array[lowestNumberIndex] = temp
    return array
