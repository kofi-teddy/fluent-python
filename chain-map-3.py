# Exploring additional features of ChainMap

# managing the list of mapping with .maps
from collections import ChainMap


for_adoption = {'dogs': 10, 'cats': 7, 'pythons': 3}
vet_treatment = {'dogs': 4, 'turtles': 1}

pets = ChainMap(for_adoption, vet_treatment)
# print(pets.maps)

del pets.maps[1]

pets.maps.append({'hamsters': 2})
# print(pets.maps)

# # for mapping in pets.maps:
#     print(mapping)


# reverse the order of the current list of 
# mappings using .reverse()
# Reversing the internal list of mappings 
# allows you to reverse the search order 
# when you look up a given key in the chain map.
# pets.maps.reverse()
# print(pets)


# Adding New Subcontexts With .new_child()
mom = {'name': 'Jane', 'age': 31}
dad = {'name': 'John', 'age': 35}


family = ChainMap(mom, dad)
# print(family)

son = {'name': 'Mike', 'age': 0}
family = family.new_child(son)


# for person in family.maps:
#     print(person)


# Skipping Subcontexts With .parents
# This property returns a new ChainMap 
# instance with all the mappings in the 
# underlying chain map except the first one. 
print(family.parents)