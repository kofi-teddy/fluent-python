from typing import List


def word_builder(array: List[str]) -> List[str]:
    """
    Builds a word from the given array of strings.

    Args:
        array (List[str]): A list of strings.

    Returns:
        List[str]: The list of words built from the given array of strings.
    """
    collection = []
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j:
                collection.append(array[i] + array[j])

    return collection


print(word_builder(["a", "b", "c", "d",]))