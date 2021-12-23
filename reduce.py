'''
The reduce(fun,seq) function is used to apply a particular function passed 
in its argument to all of the list elements mentioned in the sequence passed 
along.This function is defined in “functools” module.
'''


from functools import reduce
from operator import add, mul
import itertools 

numbers = [1,2,3,4,5,6]

# using reduce to compute the sum of the numbers
print('the sum of the numbers is: ')
print(reduce(lambda a, b: a + b, numbers))

# using reduce to compute the maximum number of the list elements
print('the maximum number of the list of numbers: ')
print(reduce(lambda a, b: a if a > b else b, numbers))


# using reduce to compute sum of list
# using operator functions
print('the sum of the list of numbers is :')
print(reduce(add, numbers))

# using reduce to compute multipy of list
# using operator functions
print('the multiplications of the list of numbers is :')
print(reduce(mul, numbers))

# using reduce to compute concatenate strings of list
# using operator functions
print('the concatenations of the list of numbers is :')
print(reduce(add, ['sky', 'crew', ' ', 'techologies']))


# python code to demonstrate summation
# using reduce() and accumulate()
print('the summation of the list using accumulate :')
print(list(itertools.accumulate(numbers, lambda x, y: x + y)))


# python program to illustrate sum of two numbers
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value

# Note that the initializer, when not None, is used as the first value instead of the
# first value from iterable, and ater the whole iterable.
tup = (2, 1, 0, 2, 2, 0, 0, 2)
print(reduce(lambda x, y: x + y, tup, 6))
