def factorial(number: int) -> int:
    """
    Calculate the factorial of a given number.

    Args:
        number (int): The number to calculate the factorial for.

    Returns:
        int: The factorial of the given number.
    """
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)
    

print(factorial(5))  # Output: 120