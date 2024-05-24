class Heap:
    def __init__(self):
        self.data = []

    def parent_index(self, child_index):
        return (child_index - 1) // 2

    def insert(self, value):
        """
        Insert a value into the heap.

        Args:
            value: The value to be inserted.
        """
        # Turn value into last node by inserting it at the end of the array:
        self.data.append(value)
        # Keep track of the index of the newly inserted node:
        new_node_index = len(self.data) - 1
        # The following loop executes the "trickle up" algorithm.
        # If the new node is not in the root position,
        # and it's greater than its parent node:
        while new_node_index > 0 and self.data[new_node_index] > self.data[self.parent_index(new_node_index)]:
            # Swap the new node with the parent node:
            self.data[self.parent_index(new_node_index)], self.data[new_node_index] = self.data[new_node_index], \
                  self.data[self.parent_index(new_node_index)]
            # Update the index of the new node:
            new_node_index = self.parent_index(new_node_index)

    def delete(self):
        """
        Delete the root node from the heap.
        """
        # We only ever delete the root node from a heap, so we
        # pop the last node from the array and make it the root node:
        self.data[0] = self.data.pop()
        # Track the current index of the "trickle node":
        trickle_node_index = 0
        # The following loop executes the "trickle down" algorithm:
        # We run the loop as long as the trickle node has a child that is greater than it:
        while self.has_greater_child(trickle_node_index):
            # Save larger child index in variable:
            larger_child_index = self.calculate_larger_child_index(trickle_node_index)
            # Swap the trickle node with its larger child:
            self.data[trickle_node_index], self.data[larger_child_index] = self.data[larger_child_index], self.data[trickle_node_index]
            # Update trickle node's new index:
            trickle_node_index = larger_child_index

    def has_greater_child(self, index: int) -> bool:
        """
        Check whether the node at index has left and right children and if either of those children are 
        greater than the node at index.

        Args:
            index (int): The index of the node.

        Returns:
            bool: True if the node at index has a child that is greater than it, False otherwise.
        """
        left_child_index = self.left_child_index(index)
        right_child_index = self.right_child_index(index)
        return ((left_child_index < len(self.data) and self.data[left_child_index] > self.data[index]) or
                (right_child_index < len(self.data) and self.data[right_child_index] > self.data[index]))

    def calculate_larger_child_index(self, index: int) -> int:
        """
        Calculate the index of the larger child of the node at the given index.

        Args:
            index (int): The index of the node.

        Returns:
            int: The index of the larger child.
        """
        left_child_index = self.left_child_index(index)
        right_child_index = self.right_child_index(index)
        # If there is no right child:
        if right_child_index >= len(self.data):
            # Return left child index:
            return left_child_index
        # If right child value is greater than left child value:
        if self.data[right_child_index] > self.data[left_child_index]:
            # Return right child index:
            return right_child_index
        else:
            # If the left child value is greater or equal to right child:
            # Return the left child index:
            return left_child_index