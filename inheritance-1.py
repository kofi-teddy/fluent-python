# python program to demonstrate
# inheritance


# bas class or parent class
class Child:

    # constructor
    def __init__(self, name):
        self.name = name

    # get name
    def getName(self):
        return self.name

    # check if thi person is Student
    def isStudent(self):
        return False 


# Derived class or child class
class Student(Child):

    # true is returned 
    def isStudent(self):
        return True


# Driver code 
# an object of child 
# std = Child('Teddy')
# print(std.getName(), std.isStudent())


# An object of Student 
# std = Student('Mawuli')
# print(std.getName(), std.isStudent())


# python program to demonstrate
# single inheritance 

# base class 
class Parent:
    def func1(self):
        print('This function is in parent class.')


# Derived class 
class Child(Parent):
    def func2(self):
        print('This function is in child class.')


# Derivers code
# object = Child()
# object.func1()
# object.func2()


# python program to demonstrate
# multiple inheritance

# base class1
class Mother:
    mothername = ''
    
    def mother(self):
        print(self.mothername)


# base class2
class Father:
    fathername = ''

    def father(self):
        print(self.fathername)


class Son(Mother, Father):

    def parents(self):
        print(f'{self.fathername}')
        print(f'Mother {self.mothername}')


# Drived class
class Son(Mother, Father):

    def parents(self):
        print(f'Father: {self.fathername}')
        print(f'Mother: {self.mothername}')


# Driver code 
# s1 = Son()
# s1.fathername = 'John'
# s1.mothername = 'Caro'
# s1.parents()


# python program to demonstrate 
# multilevel inheritance

# Base class 
class Grandfather:

    def __init__(self, grandfathername):
        self.grandfathername = grandfathername


# intermediate class
class Father(Grandfather):

    def __init__(self, fathername, grandfathername):
        self.fathername = fathername

        # invoking constructor of grandfother class
        Grandfather.__init__(self, grandfathername)


# Derived class
class Son(Father):
    
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname

        # invoking constructor of father class
        Father.__init__(self, fathername, grandfathername)

    
    def print_name(self):
        print(f'Grandfather name: {self.grandfathername}')
        print(f'Father name: {self.fathername}')
        print(f'Son name: {self.sonname}')


# Driver code 
# s1 = Son('Tyra', 'John', 'Felix')
# print(s1.grandfathername)
# s1.print_name()


# python program to demonstrate 
# hierarchical inheritance

# base class 
class Parent:

    def func1(self):
        print('This function is in parent class.')


# Derived class
class Child1(Parent):
    
    def func2(self):
        print('This function is in child 1.')


# Derived class2
class Child2(Parent):

    def func3(self):
        print('This function is in child 2.')


# Drivers code
# object1 = Child1()
# object2 = Child2()
# object1.func1()
# object1.func2()
# object2.func1()
# object2.func3()


# python program to demonstrate 
# hybrid inheritance

class School:

    def func1(self):
        print('Thid function is in school.')


class Student1(School):

    def func2(self):
        print('this function is in student 1.')


class Student2(School):

    def func3(self):
        print('This function is in student 2.')


class Student3(Student1, School):
    def func4(self):
        print('This function is in student 3.')


# Drivers code 
object = Student3()
object.func1()
object.func2()
