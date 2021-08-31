# Sorting by key and lambda functions


# def sorter(item):
#     return item["name"]


# presenters = [
#     {"name": "Susan", "age": 50},
#     {"name": "Christopher", "age": 47}
# ]

# presenters.sort(key=sorter)
# print(presenters)


# Using lambda functions
presenters = [
    {"name": "Susan", "age": 50},
    {"name": "Christopher", "age": 47}
]
print("----Alphabetically----")
presenters.sort(key=lambda item: item['name'])
print(presenters)

print("----Lenght of the name----")
presenters.sort(key=lambda item: len(item['name']))
print(presenters)
