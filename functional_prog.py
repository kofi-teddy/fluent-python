
# Python program to demonstrate
# pure functions
  

# A pure function that does Not
# changes the input list and 
# returns the new List

def pure_func(list):

    new_list = []

    for i in list:
        new_list.append(i**2)

    return new_list


original_list = [1, 2, 3]
modified_list = pure_func(original_list)

print('original list', original_list)
print('modified list', modified_list)



# Python program to demonstrate
# recursion

# Recursive function to find
# sum of a list
def sum(L, i, n, count):

    # Base case
    if n <= i:
        return count

    count += L[i]

    # going into the recursion
    count = sum(L, i +1, n, count)

    return count 

# Driver's code
L = [1, 2, 3, 4, 5]
count = 0
n = len(L)
print(sum(L, 0, n, count))


# Python program to demonstrate
# higher order functions 
def shout(text):
    return text.upper() 


def  whisper(text):
    return text.lower()


def greet(func):
    # storing the function in a variable
    greeting = func('Hi, I am created by a function passed as an argument.')
    print(greeting)


greet(shout)
greet(whisper)


# Python program to demonstrate working 
# of map.

# Return double of n
def addition(n):
    return n + n 


# We double all numbers using map()
numbers = (1, 2, 3, 4)
results = map(addition, numbers)

# Does not Print the values 
print(results)

# For printing values
for result in results:
    print(result)



# Python program to demonstrate Working
# of the filter

# function that filters vowels
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']

    if (variable in letters):
        return True
    else:
        return False


# sequence 
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

# using filter functions 
filtered = filter(fun, sequence)
print('The filtered letters are:')

for s in filtered:
    print(s)


# python code to demonstrate
# lambda

cube = lambda x: x * x * x
print(cube(7))

l = [1, 2, 3, 4, 5, 6]
is_even = [x for x in l if x % 2 == 0]

print(is_even)


# python program to demonstrate 
# immutable data types

# String data types 
# immutable = 'skycrewtechnologies'

# # changing the values will change the
# # raise an error
# immutable[1] = 'K'


# checking the types 
num = 23
print ('type of num is :', type(num))

lst = [1, 2, 3]
print('Type of lst is :', type(lst))

name = 'Atual'
print('type of name is', type(name))



class Student:
    pass

stu_obj = Student()

# Print type of object of student class
print('type of stu_obj is :', type(stu_obj))
print('Type of student class is :', type(Student))



# Defined class without any
# class methods and variables
class test:pass

# Defining method variable 
test.x = 45

# Defining class methods
test.foo = lambda self: print('Hello')

# creating object 
myobj = test()

print(myobj.x)
myobj.foo()


def test_method(self):
    print('this is test class method!')


# creating a base class 
class Base:
    def myfun(self):
        print('This is inherited method')


# Creating test class dynamically using
# type() method directly
Test = type('Test', (Base, ), dict(x='atul', my_method=test_method))

# print type of test 
print('type of test class: ', type(Test))


# Creating instance of test class 
test_obj = Test()
print('type of test_obj: ', type(test_obj))

# calling inherited methods
test_obj.myfun()

# calling test class method
test_obj.my_method()

# printing variable 
print(test_obj.x)


# our metaclass 
class MultiBases(type):
    # overriding __new__ method
    def __new__(cls, clsname, bases, clsdict):
        # if no of base classes is greater than 1
        # raisse error
        if len(bases) > 1:
            raise TypeError('Inherited multiple base classes!!!')

        # else exexute __new__ method of super class, ie.
        # call __init__ of type class
        return super().__new__(cls, clsname, bases, clsdict)


# metaclass can be specified by 'metaclass' keyword argument
# now multibase classs is used for creating classes
# this will be propagated to all subclasses of Base 
# class Base(metaclass=MultiBases):
#     pass

# # no error is raised 
# class A(Base):
#     pass

# class B(Base):
#     pass

# # this will raise an error!
# class C(A, B):
#     pass


from functools import wraps

def debug(func):
    '''decorator for debugging passed function'''

    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Full name of this method: ', func.__qualname__)
        return func(*args, **kwargs)
    return wrapper


def debugmethods(cls):
    '''
    class decorator make use of debug decorator
    to debug class methods
    '''

    # check in class dictionary for any callable(method)
    # if exist, replace it with debugged version
    for key, val in vars(cls).items() :
        if callable(val):
            setattr(cls, key, debug(val))

    return cls 

# sample class
@debugmethods
class Calc:
    def add(self, x, y):
        return x + y

    def mul(self, x, y):
        return x*y 

    def div(self, x, y):
        return x/y

mycal = Calc()
print(mycal.add(2, 3))
print(mycal.mul(5, 2))