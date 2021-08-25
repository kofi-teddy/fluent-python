#  Unpacking


# a, b = (1, 2)

# print(a)
# print(b)

# # Unpacking values not needed with _
# a, _ = (1, 2)
# print(a)

# # Unpacking more values than variables
# a, b, *c = (1, 2, 3, 4, 5)
# print(a)
# print(b)
# print(c)

# # Unpacking more values into variables while ignoring remaining values
# a, b, *_ = (1, 2, 3, 4, 5)
# print(a)
# print(b)

# Unpacking more values into variables while ignoring 
# remaining values and assigning the last value to 
# the last variable
a, b, *c, d = (1, 2, 3, 4, 5)
print(a)
print(b)
print(c)
print(d)