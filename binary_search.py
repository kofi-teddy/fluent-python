def binary_search(arr, target):
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