# data structures 

# creating list 
List = [1, 2, 3, 'Teddy', 2.3]
# print(List)


# creating a list with 
# the use of multiple values 
List = ['Teddy', 'Mawuli', 'Agudogo']
# print('\nList containing multiple values: ')
# print(List)


# creating a muiti-dimensional list 
# by nesting a list inside a list
List2 = [['Teddy', 'Mawuli'], ['Agudogo']]
# print('\nMulti-Demesional list: ')
# print(List2)

# accessing a element from the 
# list usinf index number
# print('Accessing element from the list')
# print(List[0])
# print(List[2])


# accessing a element using 
# negative indexing 
# print('Accessing element using negative indexing')

# print the last element of list 
# print(List[-1])

# pritn the third last element of list 
# print(List[-2])


# creating a dictionary
Dict = {'Name': 'Teddy', 1: [1, 2, 3, 4]}
# print('Creating dictionary')
# print(Dict)

# accessing a element using key
# print('Accessing a element using key:')
# print(Dict['Name'])


# accessing a element using get() method 
# print('Accessing a element using get:')
# print(Dict.get(1))


# creation using dictionary comprehension
# myDict = {x: x**2 for x in [1, 2, 3, 4, 5]} 
# print(myDict)


# creating a tuple with 
# the use of strings
Tuple = ('Teddy', 'Mawuli')
# print('\nTuple with use of String: ')
# print(Tuple)

# creating a tuple with 
# the use of list
list1 = [1, 2, 3, 4, 5]
# print('\nTuple with use of List: ')
Tuple = tuple(list1)

# accessing element using indexing
# print('First element of tuple: ')
# print(Tuple[0])


# accessing element using indexing
# negative indexing
# print('\n Last element of tuple')
# print(Tuple[-1])

# print('\nThird last element of tuple')
# print(Tuple[-3])


# creating s set with 
# a mixed type of values 
# having numbers and strings
Set = set([1, 2, 'teddy', 4, 'Mawuli', 6, 'teddy'])
# print('\nSet with the use of mixed values')
# print(Set)

# accessing element using 
# for loop 
# print('\nElement of set: ')
# for i in Set:
#     print(i, end=" ")
# print()

# checking the element
# using in keyword
# print('teddy' in Set)


# frozen sets
normal_set = set(['a', 'b', 'c'])

# print('Normal Set')
# print(normal_set)

# a frozen set 
frozen_set = frozenset(['e', 'f', 'g'])
# print('\nFrozen Set')
# print(frozen_set)


# string operations
String = 'welcome to skycrew technologies'
# print('creating string: ')
# print(String)

# printing first character 
# print('\n First character of string is: ')
# print(String[0])

# print last character
# print('\n Last character of string is: ')
# print(String[-1])


# bytearray operations
a = bytearray((12, 8, 25, 2))
# print('creating bytearray')
# print(a)

# accessing elements 
# print(f'\nAccessing elements: {a[1]}')

# modifying elements
a[1] = 3
# print('\nAfter modifying: ')
# print(a)

# appending elements
a.append(30)
# print('\nAfter adding elements: ')
# print(a)


# python counter operations
from collections import Counter

# with sequence of items 
# print(Counter(['B','B','A','B','C','A','B','B','A','C']))

# wiht dictionary 
count = Counter({'A': 3, 'B': 5, 'C': 2})
# print(count)

count.update(['A', 1])
# print(count)


# OrederedDict
from collections import OrderedDict

# print('Before deleting :\n')
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

# for key, value in od.items():
#     print(key, value)

# print('\nAfter deleting: \n')
# od.pop('c')

# for key, value in od.items():
#     print(key, value)

# print('\nAfter re-inserting:\n')
od['c'] = 3

# for key, value in od.items():
#     print(key, value)


# DefaultDict
from collections import defaultdict

# defining the dict
d = defaultdict(int)

L = [1, 2, 3, 4, 2, 4, 1, 2]

# iterate through the list
# for keeping the count
for i in L:

    # the dafault value is 0
    # so there is no need to
    # enter the key first
    d[i] += 1

# print(d)


from collections import ChainMap


d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

# defining the chainmap 
c = ChainMap(d1, d2, d3)
# print(c)

# print(c['a'])
# print(c['g'])


# namedTuple operations
from collections import namedtuple

# declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])

# adding values
s = Student('Kofi', '19', '21241134')

# accessing using index 
# print('The student age using index is: ',end='')
# print(s[1])

# accessing using name
# print('The student name using keyname is: ',end='')
# print(s.name)


# Deque operations
import collections

# initializing deque
de = collections.deque([1, 2, 3])

# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)

# printing modified Deque
# print('The deque after appending at right is: ')
# print(de)

# using appendleft() to insert element at left end
# inserts 6 at the beginning of deque 
de.appendleft(6)

# printing modified deque
# print('the deque after appending at left is: ')
# print(de)

# using pop() to delete elements from right end
# deletes 4 from the right end of deque 
de.pop()

# printing modified deque
# print('The deque after deleting from right is: ')
# print(de)

# using popleft() to delete element from left end 
# delete 6 from the left end of deque 
de.popleft()

# printing modified deque
# print('The deque after deleting from left is: ')
# print(de)


# python UserDict
from collections import UserDict

# creating a Dictionary where 
# deletion is not allowed 
class MyDict(UserDict):

    # function to stop deletion 
    # from dictionary
    def __del__(self):
        raise RuntimeError('Deletion not allowed')

    # function to stop pop form
    # dictionary
    def pop(self, s=None):
        raise RuntimeError('Deletion not allowed')

    # functoin to stop popitem 
    # from dictionary
    def popitem(self, s=None):
        raise RuntimeError('Deletion not allowed')


# Driver code 
# d = MyDict({
#     'b': 2, 
#     'c': 3
# })

# print('Original Dictionary')
# print(d)

# d.pop(1)


# python UserList
# python program to demonstrate
# userlist
from collections import UserList


# creating a list where 
# deletion is not allowed
class MyList(UserList):

    # function to stop deletion
    # from List
    def remove(self, s=None):
        raise RuntimeError('Deletion not allowed')

    # function to stop pop from 
    # List
    def pop(self, s=None):
        raise RuntimeError('Deletion not allowed')

# Driver code 
l = MyList([1, 2, 3, 4])

# print('Original list')
# print(l)

# inserting to list1
# l.append(5)
# print('After Insertion')
# print(l)

# deleting from list
# l.remove()


# python UserString
from collections import UserString


# creating a Mutable String 
class Mystring(UserString):

    # function to append to 
    # string
    def append(self, s):
        self.data += s

    # fucntion to remove from 
    # string
    def remove(self, s):
        self.data = self.data.replace(s, '')

# drivers code
s1 = Mystring('teddy')
print('Original String: ', s1.data)

# appending to string
s1.append('s')
# print('String After Appending: ', s1.data)

# removing from string
s1.remove('e')
print('String after removing: ', s1.data)

