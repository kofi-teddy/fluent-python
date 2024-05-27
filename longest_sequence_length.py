from typing import List


def longest_sequence_length(array: List[int]) -> int:
    """
    Find the length of the longest sequence of consecutive numbers in the array.

    Args:
        array (List[int]): The array of numbers.

    Returns:
        int: The length of the longest sequence.
    """
    hash_table = {number: True for number in array}
    greatest_sequence_length = 0

    for number in array:
        if not hash_table.get(number - 1):
            current_sequence_length = 1
            current_number = number

            while hash_table.get(current_number + 1):
                current_number += 1
                current_sequence_length += 1

                if current_sequence_length > greatest_sequence_length:
                    greatest_sequence_length = current_sequence_length

    return greatest_sequence_length


print(longest_sequence_length([10, 5, 12, 3, 55, 30, 4, 11, 2]))