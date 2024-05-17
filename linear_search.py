
def linear_search(arr, target):
    """
    Perform a linear search on the given ordered array to find the target element.

    Args:
        arr (list): The ordered array to be searched.
        target: The element to be searched for.

    Returns:
        The index of the target element if found, None otherwise.
    """
    
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        elif arr[i] > target:
            return None
    return None


print(linear_search([3, 17, 75, 80, 202], 75))