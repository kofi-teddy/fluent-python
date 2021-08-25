# Using zip to unpack two or more list simultaneously


names = ["Peter Parker", "Clark Kent", "Wade Wilson", "Bruce Wayne"]
heroes = ["Spiderman", "Superman", "Batman", "Deadpool"]
universes = ["Marvel", "DC", "Marvel", "DC"]


# for index, name in enumerate(names):
#     hero = heroes[index]
#     print(f"{name} is actually is {hero}")

# for name, hero, universe in zip(names, heroes, universes):  
#     print(f"{name} is actually is {hero} from {universe}")

for value in zip(names, heroes, universes):  
    print(value)