def find_missing_letter(some_string: str) -> str:
    """
    Finds the missing letter in the string containing all alphabet.

    Args:
        some_string: A string of letters.

    Returns:
        The missing letter in the string.
    """
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    hash_table = {}
    for char in some_string:
        hash_table[char] = True
    
    for char in alphabet:
        if char not in hash_table:
            return char
    
    return None
    

some_string = "the quick brown box jumps over a lazy dog"
print(find_missing_letter(some_string))