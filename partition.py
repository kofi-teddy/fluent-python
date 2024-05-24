from typing import List


class SortableArray:
    def __init__(self, array: List[int]):
        """
        Initialize the SortableArray with an array of integers.

        Args:
            array: The array of integers.
        """
        self.array = array

    def partition(self, left_pointer: int, right_pointer: int) -> int:
        """
        Perform partitioning on the array using the quicksort algorithm.

        Args:
            left_pointer: The left pointer index.
            right_pointer: The right pointer index.

        Returns:
            The index of the pivot after partitioning.
        """
        # We always choose the right-most element as the pivot.
        # We keep the index of the pivot for later use:
        pivot_index = right_pointer

        # We grab the pivot value itself:
        pivot = self.array[pivot_index]

        # We start the right pointer immediately to the left of the pivot
        right_pointer -= 1

        while True:
            # Move the left pointer to the right as long as it
            # points to a value that is less than the pivot:
            while self.array[left_pointer] < pivot:
                left_pointer += 1

            # Move the right pointer to the left as long as it
            # points to a value that is greater than the pivot:
            while self.array[right_pointer] > pivot:
                right_pointer -= 1

            # We've now reached the point where we've stopped
            # moving both the left and right pointers.
            # We check whether the left pointer has reached
            # or gone beyond the right pointer. If it has,
            # we break out of the loop so we can swap the pivot later
            # on in our code:
            if left_pointer >= right_pointer:
                break

            # If the left pointer is still to the left of the right
            # pointer, we swap the values of the left and right pointers:
            else:
                self.array[left_pointer], self.array[right_pointer] = \
                    self.array[right_pointer], self.array[left_pointer]

            # We move the left pointer over to the right, gearing up
            # for the next round of left and right pointer movements:
            left_pointer += 1

        # As the final step of the partition, we swap the value
        # of the left pointer with the pivot:
        self.array[left_pointer], self.array[pivot_index] = \
            self.array[pivot_index], self.array[left_pointer]

        # We return the left_pointer for the sake of the quicksort method
        # which will appear later in this chapter:
        return left_pointer
    
    def quicksort(self, left_index: int, right_index: int):
        """
        Perform quicksort on the array.

        Args:
            left_index: The left index of the subarray.
            right_index: The right index of the subarray.
        """
        # Base case: the subarray has 0 or 1 elements
        if right_index - left_index <= 0:
            return

        # Partition the range of elements and grab the index of the pivot:
        pivot_index = self.partition(left_index, right_index)

        # Recursively call this quicksort method on the left side of the pivot:
        self.quicksort(left_index, pivot_index - 1)

        # Recursively call this quicksort method on the right side of the pivot:
        self.quicksort(pivot_index + 1, right_index)

        def quickselect(kth_lowest_value: int, left_index: int, right_index: int, array: List[int]) -> int:
            """
            Selects the kth lowest value from the given subarray using the Quickselect algorithm.

            Args:
                kth_lowest_value (int): The value to select.
                left_index (int): The left index of the subarray.
                right_index (int): The right index of the subarray.
                array (List[int]): The input array.

            Returns:
                int: The kth lowest value.

            Raises:
                IndexError: If the indices are out of range.

            """
            if right_index - left_index <= 0:
                return array[left_index]

            pivot_index = self.partition(left_index, right_index, array)

            if kth_lowest_value < pivot_index:
                return quickselect(kth_lowest_value, left_index, pivot_index - 1, array)
            elif kth_lowest_value > pivot_index:
                return quickselect(kth_lowest_value, pivot_index + 1, right_index, array)
            else:  # if kth_lowest_value == pivot_index
                return array[pivot_index]

