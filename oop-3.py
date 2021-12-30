# python program to 
# demonstrate instantiating 
# a class 


class Dog:

    # A simple class 
    # attribute
    attr1 = 'mammal'
    attr2 = 'dog'

    # A sample method
    def fun(self):
        print(f'I am a {self.attr1}')
        print(f'I am a {self.attr2}')


# Driver code 
# Object instantiation
Rodger = Dog()

# Accessing class attributes
# and method through objects
# print(Rodger.attr1)
# Rodger.fun()


# A sample class with init method
class Person:

    # init method or constructor
    def __init__(self, name):
        self.name = name
    
    # Sample method
    def say_hi(self):
        print(f'Hello, my name is {self.name}')


p = Person('Teddy')
# p.say_hi()


# python code to show instance and class variables
class Dog:

    # class variable
    animal = 'dog'

    # The init method or constructor
    def __init__(self, breed, color):

        # instance variable
        self.breed = breed
        self.color = color


# object of Dog class
Rodger = Dog('Pug', 'brown')
Buzo = Dog('Bulldog', 'black')

# print('Rodger details:')
# print(f'Rodger is a {Rodger.animal}')
# print(f'Breed" {Rodger.breed}')
# print(f'Color: {Rodger.color}')

# print('\nBuzo details:')
# print(f'Buzo is a {Buzo.animal}')
# print(f'Breed" {Buzo.breed}')
# print(f'Color: {Buzo.color}')

# # class variable can be accessed using class
# # name also
# print('\nAccessing class variable using class name')
# print(Dog.animal)



# create instance variables inside methods


# class for Dog 
class Dog:

    # class variable 
    animal = 'dog'

    # the init method or constructor
    def __init__(self, breed):

        # instance variable
        self.breed = breed 

    # Adds an instance variable
    def setColor(self, color):
        self.color = color

    # Retrieves instance variable
    def getColor(self):
        return self.color


# Driver code
Rodger = Dog('pug')
Rodger.setColor('brown')
print(Rodger.getColor())