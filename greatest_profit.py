from typing import List


def find_greatest_profit(array: List[int]) -> int:
    """
    Find the greatest profit that could have been made from buying and then 
    selling a single share.

    Args:
        array (List[int]): The array of share prices.

    Returns:
        int: The greatest possible profit.
    """
    buy_price = array[0]
    greatest_profit = 0

    for price in array:
        potential_profit = price - buy_price
        if price < buy_price:
            buy_price = price
        elif potential_profit > greatest_profit:
            greatest_profit = potential_profit

    return greatest_profit