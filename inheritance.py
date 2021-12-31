# python program to demonstrate inheritance

# base or super class. not object in bracket.
# generally, objects is made ancestor of all classes 
# in python 3.x class person is
# equivalent to class person object 
class Person(object):

    # constructor 
    def __init__(self, name):
        self.name = name 

    # to get name 
    def getName(self):
        return self.name

    # check if this person is an employee or
    def isEmployee(self):
        return False


# Inherited or subclass naote person in bracket 
class Employee(Person):

    # Here we return true
    def isEmployee(self):
        return True


# driver code
emp = Person('Teddy')  # object of person 
# print(emp.getName(), emp.isEmployee())

emp = Employee('Selly')  # object of employee 
# print(emp.getName(), emp.isEmployee())



# python code to demonstrate how parent constructors
# are called

# parent class
class Person(object):
    
    # __init__ is known as the constructor
    def __init__(self, name, innumber):
        self.name = name
        self.idnumber = innumber

    def display(self):
        print(self.name)
        print(f'{self.idnumber:,}')


# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)


# creation of an object variable or an instance
a = Employee('Rahul', 102003018, 200_000, 'intern')

# a.display()


# python program to demonstrate error if we
# forget to invoke __init__() of the parent.
class A:
    def __init__(self, n='Rahul'):
        self.name = n


class B(A):
    def __init__(self, roll):
        self.roll = roll

# object = B(23)
# print(object.name)

# python example to sho the working of multiple 
# inheritance
class Base1(object):
    def __init__(self):
        self.str1 = 'teddy'
        print('base1')

class Base2(object):
    def __init__(self):
        self.str2 = 'kofi'
        print('base2')


class Derived(Base1, Base2):
    def __init__(self):

        # calling constructors of Base1
        # and base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print('Derived')

    def printStrs(self):
        print(self.str1, self.str2)

# ob = Derived()
# ob.printStrs()

# pytho program to demonstrate inheritance

# base or super class. Note objects in bracket
# generally object is made ancestor of all class
# equivalent to class Person(object)
class Base(object):

    # constructor
    def __init__(self, name):
        self.name = name

    # to get name 
    def getName(self):
        return self.name


# inherited at sub class note person in brackets
class Child(Base):

    # constructor
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age 

    # To get name 
    def getAge(self):
        return self.age


class GrandChild(Child):

    # contructor
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address

    # to get address
    def getAddress(self):
        return self.address


# Driver code 
# g = GrandChild('kofi', 23, 'Noida')
# print(g.getName(), g.getAge(), g.getAddress())


# python program to demonstrate private members 
# of the parent class 
class C(object):
    def __init__(self):
        self.c = 21

        # d is private instance variable
        self.__d = 42


class D(C):
    def __init__(self):
        self.e = 84
        C.__init__(self)


# Driver code 
object1 = D()
# produces an error as d is private instance variable 
print(object1.d)