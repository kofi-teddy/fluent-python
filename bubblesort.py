def bubble_sort(list) -> list:
    """
    Sort the given list using the bubble sort algorithm.

    Args:
        list (list): The list to be sorted.

    Returns:
        list: The sorted list.
    """
    unsorted_list_index = len(list) - 1
    sorted = False
    
    while not sorted:
        sorted = True
        for i in range(unsorted_list_index):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                sorted = False
        unsorted_list_index -= 1
    return list


print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))