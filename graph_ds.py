from queue import Queue
from typing import Any, List, Optional


class Vertex:
    def __init__(self, value: str) -> None:
        """
        Initialize a Vertex object.

        Args:
            value (str): The value of the vertex.
        """
        self.value = value
        self.adjacent_vertices: List[Vertex] = []

    # def add_adjacent_vertex(self, vertex: Vertex) -> None:
    #     """
    #     Add an adjacent vertex to the current vertex.

    #     Args:
    #         vertex (Vertex): The vertex to add as an adjacent vertex.
    #     """
    #     self.adjacent_vertices.append(vertex)

    def add_adjacent_vertex(self, vertex: 'Vertex') -> None:
        """
        Add an adjacent vertex to the current vertex.

        Args:
            vertex (Vertex): The vertex to add as an adjacent vertex.
        """
        if vertex not in self.adjacent_vertices:
            self.adjacent_vertices.append(vertex)
            vertex.add_adjacent_vertex(self)

    def dfs_traverse(self, vertex: 'Vertex', visited_vertices: dict = None) -> None:
        """
        Perform a depth-first search traversal starting from the given vertex.

        Args:
            vertex (Vertex): The vertex to start the traversal from.
            visited_vertices (dict): A dictionary keeping track of the visited vertices.
        """
        if visited_vertices is None:
            visited_vertices = {}

        # Mark vertex as visited by adding it to the dictionary:
        visited_vertices[vertex.value] = True
        # Print the vertex's value, so we can make sure our traversal really works:
        print(vertex.value)
        # Iterate through the current vertex's adjacent vertices:
        for adjacent_vertex in vertex.adjacent_vertices:
            # Ignore an adjacent vertex if we've already visited it:
            if adjacent_vertex.value not in visited_vertices:
                # Recursively call this method on the adjacent vertex:
                self.dfs_traverse(adjacent_vertex, visited_vertices)

    def dfs(self, vertex: 'Vertex', search_value: Any, visited_vertices: dict = None) -> Optional['Vertex']:
        """
        Perform a depth-first search starting from the given vertex and return the vertex with the given value.

        Args:
            vertex (Vertex): The vertex to start the search from.
            search_value (Any): The value of the vertex to search for.
            visited_vertices (dict): A dictionary keeping track of the visited vertices.

        Returns:
            Vertex: The vertex with the given value if found, None otherwise.
        """
        if visited_vertices is None:
            visited_vertices = {}

        # Return the original vertex if it happens to be the one we're searching for:
        if vertex.value == search_value:
            return vertex

        visited_vertices[vertex.value] = True

        for adjacent_vertex in vertex.adjacent_vertices:
            if adjacent_vertex.value not in visited_vertices:
                # If the adjacent vertex is the vertex we're searching for, just return that vertex:
                if adjacent_vertex.value == search_value:
                    return adjacent_vertex
                # Attempt to find the vertex we're searching for by recursively calling this method on the adjacent 
                # vertex:
                vertex_were_searching_for = self.dfs(adjacent_vertex, search_value, visited_vertices)
                # If we were able to find the correct vertex using the above recursion, return the correct vertex:
                if vertex_were_searching_for:
                    return vertex_were_searching_for

        # If we haven't found the vertex we're searching for:
        return None
    
    def bfs_traverse(self, starting_vertex: 'Vertex') -> None:
        """
        Perform a breadth-first search traversal starting from the given vertex.

        Args:
            starting_vertex (Vertex): The vertex to start the traversal from.
        """
        queue = Queue()
        visited_vertices = {}
        visited_vertices[starting_vertex.value] = True
        queue.put(starting_vertex)

        # While the queue is not empty:
        while not queue.empty():
            # Remove the first vertex off the queue and make it the current vertex:
            current_vertex = queue.get()
            # Print the current vertex's value:
            print(current_vertex.value)
            # Iterate over current vertex's adjacent vertices:
            for adjacent_vertex in current_vertex.adjacent_vertices:
                # If we have not yet visited the adjacent vertex:
                if adjacent_vertex.value not in visited_vertices:
                    # Mark the adjacent vertex as visited:
                    visited_vertices[adjacent_vertex.value] = True
                    # Add the adjacent vertex to the queue:
                    queue.put(adjacent_vertex)