from types import MappingProxyType


power_levels = MappingProxyType(
    {
        'Teddy': 6001,
        'Benny': 6000,
    }
)

# print(power_levels['Teddy'])
# print(power_levels['Benny'])

# print(list(power_levels.keys()))

# # raises errors when assigning values
# power_levels['Teddy'] = 7500

original = {'Teddy': 9001}
proxy = MappingProxyType(original)

# print(proxy['Teddy'])

original['Benny'] = 7000

# print(proxy['Benny'])

# making mutated copies
teddy_better = MappingProxyType(power_levels | {'Benny': 7000})
# print(teddy_better)

# making more complex modifications
# copy the mapping proxy into new dict 
# make changes then convert the result into a mapping proxy
new_world = power_levels | {}
del new_world['Teddy']
del new_world['Benny']
new_world['Tuncci'] = 5500
new_world = MappingProxyType(new_world)
print(new_world)