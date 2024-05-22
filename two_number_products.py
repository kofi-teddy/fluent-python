from typing import List


# def two_number_products(array: List[int]) -> List[int]:

#     """
#     Finds the product of every combination of two numbers in the array.

#     Args:
#         array (List[int]): A list of numbers.

#     Returns:
#         List[int]: The product of every combination of two numbers in the array.
#     """
#     products = []

#     for i in range(len(array) - 1):
#         for j in range(i + 1, len(array)):
#             products.append(array[i] * array[j])

#     return products


# print(two_number_products([1, 2, 3, 4, 5]))


def two_number_products(array_1: List[int], array_2: List[int]) -> List[int]:
    """
    Finds the product of every combination of two numbers in the array.

    Args:
        array (List[int]): A list of numbers.

    Returns:
        List[int]: The product of every combination of two numbers in the array.
    """
    products = []
    for i in range(len(array_1)):
        for j in range(len(array_2)):
            products.append(array_1[i] * array_2[j])

    return products


array_1 = [1, 2, 3]
array_2 = [10, 100, 1000]


print(two_number_products(array_1, array_2))