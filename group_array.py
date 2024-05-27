# from collections import Counter
from typing import Any, List

# def group_array(array: List[Any]) -> List[Any]:
#     """
#     Group the elements of an array based on their values.

#     Args:
#         array (List[Any]): The array to group.

#     Returns:
#         List[Any]: The grouped array.
#     """
#     hash_table = Counter(array)
#     new_array = []

#     for key, count in hash_table.items():
#         new_array.extend([key] * count)

#     return new_array


def group_array(array: List[Any]) -> List[Any]:
    """
    Group the elements of an array based on their values.

    Args:
        array (List[Any]): The array to group.

    Returns:
        List[Any]: The grouped array.
    """
    hash_table = {}
    new_array = []

    for value in array:
        if value in hash_table:
            hash_table[value] += 1
        else:
            hash_table[value] = 1

    for key, count in hash_table.items():
        new_array.extend([key] * count)

    return new_array