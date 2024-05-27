from typing import List


def sort_temperatures(array: List[float]) -> List[float]:
    """
    Sort an array of temperatures.

    Args:
        array (List[float]): The array of temperatures.

    Returns:
        List[float]: The sorted array of temperatures.
    """
    hash_table = {}

    for temperature in array:
        if temperature in hash_table:
            hash_table[temperature] += 1
        else:
            hash_table[temperature] = 1

    sorted_array = []
    temperature = 97.0

    while temperature <= 99.0:
        if temperature in hash_table:
            for _ in range(hash_table[temperature]):
                sorted_array.append(temperature)
        temperature += 0.1

    return sorted_array