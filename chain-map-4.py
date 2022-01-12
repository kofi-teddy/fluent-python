# managing scope and contexts with ChainMap
from collections import ChainMap
import builtins


input = 42
pylookup = ChainMap(locals(), globals(), vars(builtins))

# retrieve input from the global namespace
pylookup['input']

# remove input from the global namespace
del globals()['input']

# retrieve input from the builtins namespace
# print(pylookup['input'])


# tracking ChainMap in the standard libray 
import string


greeting = 'Hey $name, welcome to $place!'
template = string.Template(greeting)

a = template.substitute({'name': 'Jane', 'place': 'the world'})

print(a)


# When you provide values for name and place through 
# a dictionary, .substitute() replaces them in the 
# template string. Additionally, .substitute() can 
# take values as keyword arguments (**kwargs), which 
# can cause name collisions in some situations
b = template.substitute(
    {'name': 'Jane', 'place': 'the world'},
    place='Skycrew Technologies'
)
print(b)