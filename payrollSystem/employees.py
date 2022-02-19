# OOP 
# Modeling an HR system
# Employee models
from .hr import (
    SalaryPolicy,
    CommissionPolicy,
    HourlyPolicy
)
from . productivity import (
    ManagerRole,
    SecretaryRole,
    SalesRole,
    FactoryRole
)

class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('___________________')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')
            print('')


class Employee:
    '''
    Employee base class for modeling all employees types.
    '''
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Manager(Employee, ManagerRole, SalaryPolicy):
    '''
    Permanent employees paid fixed salary weekly.
    '''
    def __init__(self, id, name, weekly_salary):
        SalaryPolicy.__init__(self, name, weekly_salary)
        super().__init__(id, name)


class Secretary(Employee, SecretaryRole, SalaryPolicy):
    '''
    Derived class from employee.
    Employees paid by the hour.
    '''
    def __init__(self, id, name, weekly_salary):
        SalaryPolicy.__init__(self, weekly_salary)
        super().__init__(id, name)


class SalesPerson(Employee, SalesRole, CommissionPolicy):
    def __init__(self, id, name, weekly_salary, commission):
        CommissionPolicy.__init__(self, weekly_salary, commission)
        super().__init__(id, name)