def are_anagrams(first_string: str, second_string: str) -> bool:
    """
    Check if two strings are anagrams.

    Args:
        first_string (str): The first string.
        second_string (str): The second string.

    Returns:
        bool: True if the strings are anagrams, False otherwise.
    """
    first_word_hash_table = {}
    second_word_hash_table = {}

    # Create hash table out of first string:
    for char in first_string:
        if char in first_word_hash_table:
            first_word_hash_table[char] += 1
        else:
            first_word_hash_table[char] = 1

    # Create hash table out of second string:
    for char in second_string:
        if char in second_word_hash_table:
            second_word_hash_table[char] += 1
        else:
            second_word_hash_table[char] = 1

    # The two strings are anagrams only if the two hash tables are identical:
    return first_word_hash_table == second_word_hash_table