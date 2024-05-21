from typing import List

# def greatestProduct(array: List[int]) -> int:
#     """
#     Calculates the greatest product of any two numbers in the given array.

#     Args:
#         array (list): A list of numbers.

#     Returns:
#         int: The greatest product of any two numbers in the array.
#     """
#     greatestProductSoFar: int = array[0] * array[1]
#     for i, iVal in enumerate(array):
#         for j, jVal in enumerate(array):
#             if i != j and iVal * jVal > greatestProductSoFar:
#                 greatestProductSoFar = iVal * jVal
#     return greatestProductSoFar


# array = [1, 2, 3, 4, 5]
# result = greatestProduct(array)
# print(result)


def greatestProduct(array: List[int]) -> int:
    """
    Calculates the greatest product of any two numbers in the given array.

    Args:
        array (list): A list of numbers.

    Returns:
        int: The greatest product of any two numbers in the array.
    """
    greatestProductSoFar: int = float('-inf')
    maxNum: int = float('-inf')
    secondMaxNum: int = float('-inf')

    for num in array:
        if num > maxNum:
            secondMaxNum = maxNum
            maxNum = num
        elif num > secondMaxNum:
            secondMaxNum = num

    greatestProductSoFar = max(greatestProductSoFar, maxNum * secondMaxNum)

    return greatestProductSoFar


array = [1, 2, 3, 4, 5]
result = greatestProduct(array)
print(result)