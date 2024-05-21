def contains_x(string: str) -> bool:
    """
    Check if the given string contains the character 'X'.

    Args:
        string (str): The input string to check.

    Returns:
        bool: True if the string contains 'X', False otherwise.
    """
    for char in string:
        if char == 'X':
            return True
        
    return False


print(contains_x("Xero"))

