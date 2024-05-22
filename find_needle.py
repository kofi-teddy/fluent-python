from typing import List


def find_needle(needle: List[str], haystack: List[str]) -> bool:
    """
    Find the needle in the haystack.

    Args:
        needle: A list of strings representing the needle.
        haystack: A list of strings representing the haystack.

    Returns:
        True if the needle is found in the haystack, False otherwise.
    """
    needle_index = 0
    haystack_index = 0
    while haystack_index < len(haystack):
        if needle[needle_index] == haystack[haystack_index]:
            found_needle = True
            while needle_index < len(needle):
                if needle[needle_index] != haystack[haystack_index + needle_index]:
                    found_needle = False
                    break
                needle_index += 1
            if found_needle:
                return True
            needle_index = 0
        haystack_index += 1
    return False


needle = "def"
haystack = "abcdefghi"
print(find_needle(needle, haystack))
