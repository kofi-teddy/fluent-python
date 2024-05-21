def is_palindrome(string: str) -> bool:
    """
    Check if a string is a palindrome.

    Args:
        string: The input string to check.

    Returns:
        True if the string is a palindrome, False otherwise.
    """
    left_index: int = 0
    right_index: int = len(string) - 1

    while left_index < len(string) / 2:
        if string[left_index] != string[right_index]:
            return False
        left_index += 1
        right_index -= 1

    return True


print(is_palindrome("racecar"))