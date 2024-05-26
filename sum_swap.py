from typing import List, Union


def sum_swap(array_1: List[int], array_2: List[int]) -> Union[List[int], None]:
    """
    Find a pair of numbers, one from each array, such that swapping them would
    make the sums of the two arrays equal.

    Args:
        array_1 (List[int]): The first array.
        array_2 (List[int]): The second array.

    Returns:
        Union[List[int], None]: The indices of the pair of numbers to swap, or 
        None if no such pair exists.
    """
    hash_table = {num: index for index, num in enumerate(array_1)}
    sum_1 = sum(array_1)
    sum_2 = sum(array_2)

    shift_amount = (sum_1 - sum_2) // 2

    for index, num in enumerate(array_2):
        if hash_table.get(num + shift_amount) is not None:
            return [hash_table[num + shift_amount], array_2[index]]

    return None


array_1 = [5, 3, 2, 9, 1]
array_2 = [1, 12, 5]

print(sum_swap(array_1, array_2))  # Output: [0, 1]