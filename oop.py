# Python Object-Oriented Programming 


class Employee:
    # class variables
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    # classmethods
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # Alternative to constructors
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # staticmethods
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# subclasses
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)        
        self.prog_lang = prog_lang


class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)  
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('kofi', 'teddy', 60000, 'Python')
dev_2 = Developer('test', 'user', 70000, 'Js')

mgr_1 = Manager('ama', 'baddoo', 90000, [dev_1])

print(mgr_1.email)
mgr_1.remove_emp(dev_2)
mgr_1.print_emps()

# print(dev_1.email)
# print(dev_1.prog_lang)

# import datetime
# my_date = datetime.date(2016, 7, 11)

# print(Employee.is_workday(my_date))


# emp_str_1 = 'selorm-agudogo-800000'
# emp_str_2 = 'wonder-agudogo-800000'
# emp_str_3 = 'eliplim-agudogo-800000'

# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.email)
# print(new_emp_1.pay)

# emp_1.set_raise_amt(1.05)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print(Employee.num_of_emps)





# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)


# print(emp_1.email)
# print(emp_2.email)

# print(emp_1.fullname())
# print(Employee.fullname(emp_1))