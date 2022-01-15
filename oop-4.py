# object oriented programming
# type hints


# def odd(n: int) -> bool:
#     return n % 2 != 0


# def main():
#     print(odd('Hello, world!'))

# if __name__ == '__main__':
#     main()


# class Point:
    
#     def reset(self):
#         self.x = 0 
#         self.y = 0


# p1 = Point()
# p2 = Point()

# p1.x = 5
# p1.y = 4

# p2.x = 5
# p2.y = 60

# print(p1.x, p1.y)
# print(p2.x, p2.y)

# p1.reset()
# p2.reset()

# print(p1.x, p1.y)
# print(p2.x, p2.y)


import math


class Point:
    '''
    Represents a point in two-dimensional geometric coordinates
    >>> p_0 = Point()
    >>> p_1 = Point(3, 4)
    >>> p_0.calculate_distance(p_1)
    5.0
    '''

    def __init__(self, x: float, y: float) -> None:
        '''
        Initialize the position of a new point. The x and y
        coordinates can be specified. If they are not, the
        point defaults to the origin.
        :param x: float x-coordinate
        :param y: float x-coordinate
        '''
        self.move(x, y)

    def move(self, x: float, y: float) -> None:
        '''
        Move the point to a new location in 2D space.
        :param x: float x-coordinate
        :param y: float x-coordinate
        '''
        self.x = x
        self.y = y 

    def  reset(self) -> None:
        '''
        Reset the point back to the geometric origin: 0, 0
        '''
        self.move(0, 0)

    def calculate_distance(self, other: 'Point') -> float:
        '''
        Calculate the Euclidean distance from this point
        to a second point passed as a parameter.
        :param other: Point instance
        :return: float distance
        '''
        return math.hypot(self.x - other.x, self.y - other.y)


point = Point(3, 5)
print(point.x, point.y)


# point1 = Point()
# point2 = Point()

# point1.reset()
# point2.move(5, 0)
# print(point2.calculate_distance(point1))


# assert point2.calculate_distance(point1) == point1.calculate_distance(point2)

# point1.move(3, 4)
# print(point1.calculate_distance(point2))
# print(point1.calculate_distance(point1))
