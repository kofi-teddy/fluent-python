# Mutable and Immutable

employees = ['Corey', 'John', 'Rick', 'Steve', 'Carl', 'Adam']

output = '<ul>\n'

for employee in employees:
    output += '\t<li>{}</li>\n'.format(employee)
    print('Address of output is {}'.format(id(output)))

output += '</ul>'
print(output)
print('\n')


# a = [1, 2, 3, 4, 5]
# print(a)
# print('Address of a is: {}'.format(id(a)))


# a[0] = 6
# print(a)
# print('Address of a is: {}'.format(id(a)))

# a = 'teddy'
# print(a)
# print('Address of a is: {}'.format(id(a)))

# a = 'agudogo'
# print(a)
# print('Address of a is: {}'.format(id(a)))
