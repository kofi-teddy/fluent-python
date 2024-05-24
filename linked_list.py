from typing import Any, Optional


class Node:
    """
    Represents a node in a linked list.
    """

    def __init__(self, data: Any) -> None:
        """
        Initializes a new instance of the Node class.

        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.next_node: Optional[Node] = None


class LinkedList:
    def __init__(self, first_node):
        self.first_node = first_node

    def read(self, index):
        # We begin at the first node of the list: current_node = first_node
        current_node = self.first_node
        current_index = 0
        while current_index < index:
            # We keep following the links of each node until we get to the index we're looking for:
            current_node = current_node.next_node
            current_index += 1
            # If we're past the end of the list, that means the value cannot be found in the list, so return None:
            if not current_node:
                return None
        return current_node.data

    def index_of(self, value):
        # We begin at the first node of the list: current_node = first_node
        current_node = self.first_node
        current_index = 0
        while current_node:
            # If we find the data we're looking for, we return its index:
            if current_node.data == value:
                return current_index
            # Otherwise, we move on to the next node:
            current_node = current_node.next_node
            current_index += 1
        # If we get through the entire list without finding the data, we return None:
        return None
    
    def insert_at_index(self, index, value):
        # We create a new node with the given value:
        new_node = Node(value)
        # We begin at the first node of the list: current_node = first_node
        current_node = self.first_node
        current_index = 0
        # If we're inserting at the beginning of the list, we need to update the first_node reference:
        if index == 0:
            new_node.next_node = self.first_node
            self.first_node = new_node
            return
        # Otherwise, we need to find the node just before the index where we want to insert the new node:
        while current_index < index - 1:
            current_node = current_node.next_node
            current_index += 1
            # If we're past the end of the list, we cannot insert at the given index, so we return None:
            if not current_node:
                return None
        # We insert the new node between the current node and the next node:
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

    def delete_at_index(self, index):
        # We begin at the first node of the list: current_node = first_node
        current_node = self.first_node
        current_index = 0
        # If we're deleting the first node, we need to update the first_node reference:
        if index == 0:
            self.first_node = self.first_node.next_node
            return
        # Otherwise, we need to find the node just before the index we want to delete:
        while current_index < index - 1:
            current_node = current_node.next_node
            current_index += 1
            # If we're past the end of the list, we cannot delete the node at the given index, so we return None:
            if not current_node:
                return None
        # We delete the node by updating the next_node reference of the previous node:
        current_node.next_node = current_node.next_node.next_node


node_1 = Node("once")
# node_2 = Node("upon") 
# node_3 = Node("a") 
# node_4 = Node("time")
# node_1.next_node = node_2 
# node_2.next_node = node_3 
# node_3.next_node = node_4


list = LinkedList.first_node(node_1)