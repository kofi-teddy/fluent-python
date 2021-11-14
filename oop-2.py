# Python Object-Oriented Programming 
# Magic Dunder

class Employee:
    # class variables
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    '''  
    An ambigiuous representation of the object and used for logging and debugging.
    '''
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    '''
    Readable representation of the objects and used as a display to the enduser
    '''
    def __str__(self) -> str:
        return '{} - {}'.format(self.fullname, self.email)


    def __add__(self, other):
        return self.pay + other.pay



emp_1 = Employee('kofi', 'teddy', 60000)
emp_2 = Employee('test', 'user', 70000)

print(emp_1 + emp_2)

# print(emp_1)

# print(repr(emp_1))
# print(str(emp_1))

# print(emp_1.__repr__())
# print(emp_1.__str__())
