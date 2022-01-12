# pytho program to demonstrate 
# ChainMap 
from collections import ChainMap


d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

# defining the chainmap 
c = ChainMap(d1, d2, d3)

# print(c)


# python code to demonstrate ChainMap and 
# keys(), values() and maps() 

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}

# initializing ChainMap
# chain = ChainMap(dict1, dict2)

# printing chainMap using map
# print('All the ChainMap contents are: ')
# print(chain.maps)

# printing keys using keys()
# print('All keys of ChainMap are: ')
# print(list(chain.keys()))

# printing values using values()
# print('All values of ChainMap are: ')
# print(list(chain.values()))


# python code to demonstrate ChainMap and 
# reversed() and new_child()

# initializing dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'f': 5}

# initializing ChainMap
chain = ChainMap(dict1, dict2)

# printing chainMap using map 
# print('All the ChainMAp contents are: ')
# print(chain.maps)

# using new_child() to add new dictionary 
chain1 = chain.new_child(dict3)

# print chainMap using map 
# print('Displaying new ChainMap: ')
# print(chain1.maps)

# displaying value associated with before revervsing
print('Value associated with before revervsing is: ', end='')
print(chain1['b'])

# reversing the ChainMap
chain1.maps = reversed(chain1.maps)

# displaying value associated with b after revervsing
print('Value associated with b after revervsing is: ', end='')
print(chain1['b'])