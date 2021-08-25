# Getting and setting attributes on certain objects


# class Person():
#     pass


# person = Person()

# Dynamically adding values
# person.first = "Kofi"
# person.last = "Teddy"

# print(person.first)
# print(person.last)

# first_key = "first"
# firts_val = "Kofi"
# setattr(person, first_key, firts_val)
# print(person.first)
# first = getattr(person, first_key)
# print(first)


class Person():
    pass


person = Person()

personal_info = {"first": "Kofi", "last": "Teddy"}

for key, value in personal_info.items():
    setattr(person, key, value)


print(person.first)
print(person.last)

for key in personal_info.keys():
    print(getattr(person, key))