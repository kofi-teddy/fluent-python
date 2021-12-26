# Python program showing 
# abstract base class working with

from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def noofsides(self):
        pass


class Triangle(Polygon):

    # overriding abstract method 
    def noofsides(self):
        print('I have 3 sides')


class Pentagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print('I have 3 sides')


class Hexagon(Polygon):

    # overriding abstract methods
    def noofsides(self):
        print('I have 6 sides')


class Quadrilateral(Polygon):

    # overriding abstract methods
    def noofsides(self):
        print('I have 4 sides')


# Driver code
# r = Triangle()
# r.noofsides()

# k = Quadrilateral()
# k.noofsides()

# r = Pentagon()
# r.noofsides()

# k = Hexagon()
# k.noofsides()


# python program showing 
# abstract base class works 

class Animal(ABC):

    def move(self):
        pass

class Human(Animal):

    def move(self):
        print('I can walk and run')


class Snake(Animal):

    def move(self):
        print('I can crawl')


class Dog(Animal):

    def move (self):
        print('I can bark')


class Lion(Animal):

    def move(self):
        print('I can roar')


# Driver code
# R = Human()
# R.move()

# K = Snake()
# K.move()

# r = Dog()
# r.move()

# k = Lion()
# k.move()


# python program showing 
# implementation of abstract 
# class through subclassing 
class parent:

    def geeks(self):
        pass


class child(parent):

    def geeks(self):
        print('child class')


# Driver code
# print(issubclass(child, parent))
# print(isinstance(child(), parent))


# python program invoking a 
# method using super()
class R(ABC):

    def rk(ABC):
        print('Abstract base class')


class K(R):

    def rk(self):
        super().rk()
        print('subclass')


# Driver code 
# r = K()
# r.rk()


# python program showing 
# abstract properties
import abc 


class parent(ABC):
    
    @abc.abstractproperty
    def geeks(self):
        return 'parent class'


class child(parent):

    @property
    def geeks(self):
        return 'child class'


# try:
#     r = parent()
#     print(r.geeks)
# except Exception as err:
#     print(err)


# r = child()
# print(r.geeks)


# python program showing  
# abstract class cannot 
# be an instantiation 
class Animal(ABC):
    
    @abstractmethod
    def move(self):
        pass


class Human(Animal):
    
    def move(self):
        print('I can walk and run')


class Snake(Animal):

    def move(self):
        print('I can crawl')


class Dog(Animal):

    def move(self):
        print('I can bark')


class Lion(Animal):
    
    def move(self):
        print('I can roar')


c = Animal()