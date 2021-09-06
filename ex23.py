# List Comprehension

# fruits = ['apple', 'banana', 'mango', 'grapes']
# newlist = []

# for x in fruits:
#     if "b" in x:
#         newlist.append(x)

# print(newlist)

# Using list comprehension
# newlist = [expression for item in iterable if condition == True]

fruits = ['apple', 'banana', 'mango', 'grapes']

newlist = [x for x in fruits if 'b' in x]

print(newlist) 