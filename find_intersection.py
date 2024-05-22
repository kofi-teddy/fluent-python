from typing import List


def find_instersection(array_1: List[int], array_2: List[int]) -> List[int]:
    """
    Finds the intersection of two arrays.

    Args:
        array_1 (List[int]): The first array.
        array_2 (List[int]): The second array.

    Returns:
        List[int]: The intersection of the two arrays.
    """
    result = []
    if len(array_1) > len(array_2):
        smaller_array = array_2
        larger_array = array_1
    else:
        smaller_array = array_1
        larger_array = array_2
    hash_table = {}
    for i in range(len(larger_array)): 
        hash_table[larger_array[i]] = True

    for i in range(len(smaller_array)):
        if hash_table.get(smaller_array[i]):
            result.append(smaller_array[i])
    return result


array_1 = [1, 2, 3, 4, 5]
array_2 = [0, 2, 4, 6, 8]


print(find_instersection(array_1, array_2))