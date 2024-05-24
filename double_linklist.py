from typing import Any, Optional


class Node:
    """
    Represents a node in a doubly linked list.
    """

    def __init__(self, data: Any) -> None:
        """
        Initializes a new instance of the Node class.

        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.next_node: Optional[Node] = None
        self.previous_node: Optional[Node] = None


class DoublyLinkedList:
    """
    Represents a doubly linked list.
    """

    def __init__(self, first_node: Optional[Node] = None, last_node: Optional[Node] = None) -> None:
        """
        Initializes a new instance of the DoublyLinkedList class.

        Args:
            first_node: The first node of the list.
            last_node: The last node of the list.
        """
        self.first_node: Optional[Node] = first_node
        self.last_node: Optional[Node] = last_node

    def insert_at_end(self, value: Any) -> None:
        """
        Inserts a new node with the given value at the end of the linked list.

        Args:
            value: The value to be inserted.
        """
        new_node = Node(value)

        if self.first_node is None:
            # If there are no elements yet in the linked list
            self.first_node = new_node
            self.last_node = new_node
        else:
            # If the linked list already has at least one node
            new_node.previous_node = self.last_node
            self.last_node.next_node = new_node
            self.last_node = new_node

    def remove_from_front(self) -> Optional['Node']:
        """
        Remove the node from the front of the doubly linked list.

        Returns:
            Optional[Node]: The removed node, or None if the list is empty.
        """
        removed_node = self.first_node
        if self.first_node:
            self.first_node = self.first_node.next_node
        return removed_node
    
    def print_list(self) -> None:
        """
        Print the data of each node in the doubly linked list.
        """
        current_node = self.first_node
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node

    def print_in_reverse(self) -> None:
        """
        Print the data of each node in the doubly linked list in reverse order.
        """
        current_node = self.last_node
        while current_node:
            print(current_node.data)
            current_node = current_node.previous_node
    
    def get_last(self) -> Optional[Any]:
        """
        Get the data of the last node in the doubly linked list.

        Returns:
            Optional[Any]: The data of the last node, or None if the list is empty.
        """
        current_node = self.first_node
        while current_node and current_node.next_node:
            current_node = current_node.next_node
        return current_node.data if current_node else None
    
    def reverse(self) -> None:
        """
        Reverse the order of nodes in the doubly linked list in-place.
        """
        previous_node = None
        current_node = self.first_node
        while current_node:
            next_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node
        self.first_node = previous_node

    def delete_middle_node(self, node: 'Node') -> None:
        """
        Delete a node in the middle of the doubly linked list, given only access to that node.

        Args:
            node (Node): The node to be deleted.
        """
        if node and node.next_node:
            node.data = node.next_node.data
            node.next_node = node.next_node.next_node


class Queue:
    """
    A Queue class implemented using a doubly linked list.
    """

    def __init__(self) -> None:
        """
        Initialize an empty Queue.
        """
        self.data = DoublyLinkedList()

    def enqueue(self, element: Any) -> None:
        """
        Add an element to the end of the Queue.

        Args:
            element (Any): The element to be added.
        """
        self.data.insert_at_end(element)

    def dequeue(self) -> Optional[Any]:
        """
        Remove an element from the front of the Queue.

        Returns:
            Optional[Any]: The removed element, or None if the Queue is empty.
        """
        removed_node = self.data.remove_from_front()
        return removed_node.data if removed_node else None

    def read(self) -> Optional[Any]:
        """
        Read the element at the front of the Queue without removing it.

        Returns:
            Optional[Any]: The front element, or None if the Queue is empty.
        """
        return self.data.first_node.data if self.data.first_node else None