from queue import Queue
from typing import Dict, List, Optional

from graph_ds import Vertex

# class WeightedGraphVertex:
#     """
#     A class to represent a vertex in a weighted graph.
#     """

#     def __init__(self, value: Any) -> None:
#         """
#         Initialize a vertex with a value and an empty dictionary for adjacent vertices.

#         Args:
#             value (Any): The value of the vertex.
#         """
#         self.value = value
#         self.adjacent_vertices = {}

#     def add_adjacent_vertex(self, vertex: 'WeightedGraphVertex', weight: float) -> None:
#         """
#         Add an adjacent vertex along with its weight to the current vertex.

#         Args:
#             vertex (WeightedGraphVertex): The vertex to add as an adjacent vertex.
#             weight (float): The weight of the edge connecting the current vertex and the adjacent vertex.
#         """
#         self.adjacent_vertices[vertex] = weight


# dallas = WeightedGraphVertex("Dallas")
# toronto = WeightedGraphVertex("Toronto")
# dallas.add_adjacent_vertex(toronto, 138)
# toronto.add_adjacent_vertex(dallas, 216)


class City:
    """
    A class to represent a city with routes to other cities.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a city with a name and an empty dictionary for routes.

        Args:
            name (str): The name of the city.
        """
        self.name = name
        self.routes = {}

    def add_route(self, city: 'City', price: float) -> None:
        """
        Add a route to another city along with its price to the current city.

        Args:
            city (City): The city to add a route to.
            price (float): The price of the route to the other city.
        """
        self.routes[city] = price


atlanta = City("Atlanta")
boston = City("Boston")
chicago = City("Chicago")
denver = City("Denver")
el_paso = City("El Paso")

atlanta.add_route(boston, 100)
atlanta.add_route(denver, 160)
boston.add_route(chicago, 120)
boston.add_route(denver, 180)
chicago.add_route(el_paso, 80)
denver.add_route(chicago, 40)
denver.add_route(el_paso, 140)


def dijkstra_shortest_path(starting_city: 'City', final_destination: 'City') -> List[str]:
    """
    Calculate the shortest path from the starting city to the final destination using Dijkstra's algorithm.

    Args:
        starting_city (City): The city to start from.
        final_destination (City): The city to reach.

    Returns:
        List[str]: The shortest path from the starting city to the final destination.
    """
    cheapest_prices_table = {starting_city.name: 0}
    cheapest_previous_stopover_city_table = {}
    unvisited_cities = list(starting_city.routes.keys())
    visited_cities = {}

    current_city = starting_city

    while current_city:
        visited_cities[current_city.name] = True
        unvisited_cities.remove(current_city)

        for adjacent_city, price in current_city.routes.items():
            if adjacent_city.name not in visited_cities:
                unvisited_cities.append(adjacent_city)

            price_through_current_city = cheapest_prices_table[current_city.name] + price

            if adjacent_city.name not in cheapest_prices_table or price_through_current_city < cheapest_prices_table[adjacent_city.name]:
                cheapest_prices_table[adjacent_city.name] = price_through_current_city
                cheapest_previous_stopover_city_table[adjacent_city.name] = current_city.name

        current_city = min(unvisited_cities, key=lambda city: cheapest_prices_table[city.name], default=None)

    shortest_path = []
    current_city_name = final_destination.name

    while current_city_name != starting_city.name:
        shortest_path.append(current_city_name)
        current_city_name = cheapest_previous_stopover_city_table[current_city_name]

    shortest_path.append(starting_city.name)

    return shortest_path[::-1]


def bfs(starting_vertex: 'Vertex', search_value: str, visited_vertices: Dict[str, bool] = None) -> Optional['Vertex']:
    """
    Perform a breadth-first search (BFS) from the starting vertex to find a vertex with the search value.

    Args:
        starting_vertex (Vertex): The vertex to start the search from.
        search_value (str): The value to search for.
        visited_vertices (dict, optional): A dictionary to keep track of visited vertices. Defaults to None.

    Returns:
        Vertex: The vertex with the search value if found, otherwise None.
    """
    if visited_vertices is None:
        visited_vertices = {starting_vertex.value: True}

    queue = Queue()
    queue.put(starting_vertex)

    while not queue.empty():
        current_vertex = queue.get()

        if current_vertex.value == search_value:
            return current_vertex

        for adjacent_vertex in current_vertex.adjacent_vertices:
            if adjacent_vertex.value not in visited_vertices:
                visited_vertices[adjacent_vertex.value] = True
                queue.put(adjacent_vertex)

    return None


def find_shortest_path(first_vertex: 'Vertex', second_vertex: 'Vertex', visited_vertices: Dict[str, bool] = None) -> List[str]:
    """
    Find the shortest path from the first vertex to the second vertex using breadth-first search.

    Args:
        first_vertex (Vertex): The vertex to start the search from.
        second_vertex (Vertex): The vertex to reach.
        visited_vertices (dict, optional): A dictionary to keep track of visited vertices. Defaults to None.

    Returns:
        List[str]: The shortest path from the first vertex to the second vertex.
    """
    if visited_vertices is None:
        visited_vertices = {first_vertex.value: True}

    queue = Queue()
    queue.put(first_vertex)

    previous_vertex_table = {}

    while not queue.empty():
        current_vertex = queue.get()

        for adjacent_vertex in current_vertex.adjacent_vertices:
            if adjacent_vertex.value not in visited_vertices:
                visited_vertices[adjacent_vertex.value] = True
                queue.put(adjacent_vertex)
                previous_vertex_table[adjacent_vertex.value] = current_vertex.value

    shortest_path = []
    current_vertex_value = second_vertex.value

    while current_vertex_value != first_vertex.value:
        shortest_path.append(current_vertex_value)
        current_vertex_value = previous_vertex_table[current_vertex_value]

    shortest_path.append(first_vertex.value)

    return shortest_path[::-1]