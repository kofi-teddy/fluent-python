

# def has_duplicate_value(array):
#     """
#     Check if the given list has any duplicate values.

#     Args:
#         array (list): The list to be checked for duplicate values.

#     Returns:
#         bool: True if the list has duplicate values, False otherwise.
#     """

#     steps = 0  # count of steps
#     for i in range(len(array)):
#         for j in range(len(array)):
#             steps += 1  # increment number of steps
#             if i != j and array[i] == array[j]:
#                 return True
#     print(steps)  # print number of steps if no duplicates
#     return False


# print(has_duplicate_value([1, 3, 5, 7, 8, 6]))


def has_duplicate_value_v2(array):
    """
    Check if the given list has any duplicate values.

    Args:
        array (list): The list to be checked for duplicate values.

    Returns:
        bool: True if the list has duplicate values, False otherwise.
    """

    existing_numbers = []
    steps = 0
    for i in range(len(array)):
        steps += 1
        if array[i] in existing_numbers:
            return True
        else:
            existing_numbers.append(array[i])

    print(steps)
    return False


print(has_duplicate_value_v2([1, 3, 5, 7, 8, 6]))