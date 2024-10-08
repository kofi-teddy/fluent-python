# Python Object-Oriented Programming 
# Decorators - getters, setters and deleters

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f'{self.first}.{self.last}.company'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name')
        self.first = None
        self.last = None




emp_1 = Employee('kofi', 'teddy')
emp_2 = Employee('test', 'user')

emp_1.first = 'mawuli'

emp_1.fullname = 'teddy agudogo'


print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)


del emp_1.fullname

