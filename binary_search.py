def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the index of the target element.

    Args:
        arr (list): The sorted array to search in.
        target: The element to search for.

    Returns:
        int: The index of the target element if found, -1 otherwise.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            # Element found, return its index
            return mid 
        
        elif arr[mid] < target:
            # Search the right half
            low = mid + 1 

        else:
            # Search the left half
            high = mid - 1 

    return -1