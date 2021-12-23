
# Python program to demonstrate working
# of map.

# Return a double of n
# def addition(n):
#     return n + n 

# # We double all numbers using map
# numbers = [1, 2, 3]
# result = map(addition, numbers)
# print(list(result))

# Double all numbers using map and lambda 
# numbers = [1, 2, 3, 4, 5]
# result = map(lambda x: x + x, numbers)
# print(list(result))

# Add two lists using map and lambda
# number1 = [1, 2, 3, 4, 5]
# number2 = [6, 7, 8, 9, 10]
# results = map(lambda x, y: x + y, number1, number2)
# print(list(results))

# List of strings
l = ['sat', 'sun', 'mon', 'tue', 'wed', 'thu', 'fri']
# map can listify a list of strings individually
test = list(map(list, l))

print(test)