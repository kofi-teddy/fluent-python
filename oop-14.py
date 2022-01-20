# oop
# More advance concepts oop   
from __future__ import annotations
from ctypes import Union
from math import hypot
from typing import Tuple, List, Optional, Iterable



# square = [(1,1), (1,2), (2,2), (2,1)]

# def distance(p1, p2):
#     return hypot(p1[0]-p2[0], p1[1]-p2[1])

# def perimeter(polygon):
#     pairs = zip(polygon, polygon[1:]+polygon[:1])
#     return sum(
#         distance(p1, p2) for p1, p2 in pairs
#     )


# Using type hints 
# Point = Tuple[float, float]

# def distance(p1: Point, p2: Point) -> float:
#     return hypot(p1[0] - p2[0], p1[1] - p2[1])


# Polygon = List[Point]


# def parameter(polygon: Polygon) -> float:
#     pairs = zip(polygon, polygon[1:] + polygon[:1])
#     return sum(distance(p1, p2) for p1, p2 in pairs)


# converting to oop
class Point:
    def __init__(self, x:float, y:float) -> float:
        self.x = x
        self.y = y

    def distance(self, other: 'Point') -> float:
        return hypot(self.x - other.x, self.y - other.y)


class Polygon:
    def __init__(self) -> None:
        self.vertices: List[Point] = []
    
    def add_point(self, point: Point) -> None:
        self.vertices.append((point))

    def perimeter(self) -> float:
        pairs = zip(
            self.vertices, self.vertices[1:] + self.vertices[:1]
        )
        return sum(p1.distance(p2) for p1, p2 in pairs)


class Polygon_2:
    def __init__(self, vertices: Optional[Iterable[Point]] = None) -> None:
        self.vertices = list(vertices) if vertices else []
    
    def perimeter(self) -> float:
        pairs = zip(
            self.vertices, self.vertices[1:] + self.vertices[:1])
        return sum(p1.distance(p2) for p1, p2 in pairs)


Pair = Tuple[float, float]
Point_or_Tuple = Union[Point, Pair]


class Polygon_3:
    def __init__(self, vertices: Optional[Iterable[Point_or_Tuple]] = None) -> None:
        self.vertices: List[Point] = []
        if vertices:
            for point_or_tuple in vertices:
                self.vertices.append(self.make_point(point_or_tuple))

    @staticmethod
    def make_point(item: Point_or_Tuple) -> Point:
        return item if isinstance(item, Point) else Point(*item)


# driver code
# print(perimeter(square))
# square = Polygon()
# square.add_point(Point(1, 1))
# square.add_point(Point(1, 2))
# square.add_point(Point(2, 2))
# square.add_point(Point(2, 1))
# print(square.perimeter())

square = Polygon_2(
    [Point(1,1), Point(1,2), Point(2,2), Point(2,1)]
)

print(square.perimeter())

