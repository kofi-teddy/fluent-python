'''
The filter() method filters the given sequence with the help of a function 
that tests each element in the sequence to be true or not.
filter(function, sequence)
'''

def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False

sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
filtered = filter(fun, sequence)

print(list(filtered))


# checking if the sequence contains odd numbers
seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("odd numbers: ", list(filter(lambda x: x % 2 != 0, seq)))

# checking if the sequence contains evennumbers
seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("even numbers: ", list(filter(lambda x: x % 2 == 0, seq)))

