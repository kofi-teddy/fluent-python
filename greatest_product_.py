from typing import List


def greatest_product(array: List[int]) -> int:
    """
    Find the greatest product that can be made from two numbers in the array.

    Args:
        array (List[int]): The array of numbers.

    Returns:
        int: The greatest possible product.
    """
    greatest_number = float('-inf')
    second_to_greatest_number = float('-inf')
    lowest_number = float('inf')
    second_to_lowest_number = float('inf')

    for number in array:
        if number >= greatest_number:
            second_to_greatest_number = greatest_number
            greatest_number = number
        elif number > second_to_greatest_number:
            second_to_greatest_number = number

        if number <= lowest_number:
            second_to_lowest_number = lowest_number
            lowest_number = number
        elif number > lowest_number and number < second_to_lowest_number:
            second_to_lowest_number = number

    greatest_product_from_two_highest = greatest_number * second_to_greatest_number
    greatest_product_from_two_lowest = lowest_number * second_to_lowest_number

    # return max(greatest_product_from_two_highest, greatest_product_from_two_lowest)
    if greatest_product_from_two_highest > greatest_product_from_two_lowest:
        return greatest_product_from_two_highest
    else:
        return greatest_product_from_two_lowest