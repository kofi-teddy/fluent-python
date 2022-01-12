from collections import ChainMap, OrderedDict, defaultdict


# print(ChainMap())

# # use rgular dictionaries 
# numbers = {'one': 1, 'two': 2}
# letters = {'a': 'A', 'b': 'B'}

# print(ChainMap(numbers, letters))

# creating several ChainMap objects using different
# combinations of mappings.
# numbers = OrderedDict(one=1, two=2)
# letters = defaultdict(str, {'a': 'A', 'b': 'B'})
# print(ChainMap(numbers, letters))


# creating ChainMap objects using the class 
# method .fromkeys(). This method can take an iterable of keys
# and an optional default value for all the keys.
# a = ChainMap.fromkeys(['one', 'two', 'three'])
# print(a)

# a = ChainMap.fromkeys(['one', 'two', 'three'], 0)
# print(a)


# Once you have a ChainMap object, 
# you can retrieve existing keys 
# with dictionary-style key lookup, 
# or you can use .get()
# numbers = {'one': 1, 'two': 2}
# letters = {'a': 'A', 'b': 'B'}

# num = ChainMap(numbers, letters)
# print(num['two'])

# print(num.get('a'))

# generates KeyError
# print(num['three'])


# When you access a duplicate key, such as "dogs" 
# and "cats", the chain map only returns the first
# occurrence of that key. 
for_adoption = {'dogs': 10, 'cats': 7, 'pythons': 3}
vet_treatment = {'dogs': 4, 'cats': 3, 'turtles': 1}
pets = ChainMap(for_adoption, vet_treatment)

# print(pets)
# print(pets['dogs'])
# print(pets['cats'])
# print(pets['turtles'])

# The for loop iterates over the dictionaries in 
# pets and prints the first occurrence of each 
# key-value pair. You can also iterate through 
# the dictionary directly or with .keys() and 
# .values() as you can do with any dictionary:
# for key, value in pets.items():
#     print(f'{key} -> {value}')

# or
# for key in pets:
#     print(f'{key} -> {pets[key]}')


# ChainMap also supports mutations. In other words,
# it allows you to update, add, delete, and pop 
# key-value pairs.
# The difference in this case is that these 
# operations act on the first mapping only

# use rgular dictionaries 
# numbers = {'one': 1, 'two': 2}
# letters = {'a': 'A', 'b': 'B'}
# num = ChainMap(numbers, letters)
# print(num)

# updating an exiting key 
# num['b'] = 'b'
# num['c'] = 'C'
# print(num)

# pop keys
# print(num.pop('two'))

# delete keys
# del num['c']
# print(num)

# clear the dictionary
# num.clear()
# print(num)

# Operations that mutate the content of a given chain
# map only affect the first mapping, even if the key 
# you’re trying to mutate exists in other mappings 
# in the list. 
numbers = {'one': 1, 'two': 2}
letters = {'a': 'A', 'b': 'B'}

num = ChainMap({}, numbers, letters)
# print(num)

num['comma'] = ','
num['period'] = '.'

# print(num)


# As an alternative to chaining multiple dictionaries
# with ChainMap, you can consider merging them together 
# using dict.update()
for_adoption = {'dogs': 10, 'cats': 7, 'python': 3}
vet_treatment = {'cats': 2, 'dogs': 1,'hamsters': 2, 'turtles': 1}

a = ChainMap(for_adoption, vet_treatment)
# print(a)


# The first and most important drawback is that you’re 
# throwing out the ability to manage and prioritize the 
# access to repeated keys using multiple scopes or 
# contexts. With .update(), the last value you provide 
# for a given key will always prevail

# merge dictionaries with .update() 
pets = {}
pets.update(for_adoption)
pets.update(vet_treatment)
print(pets)