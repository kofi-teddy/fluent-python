# OOP 
# Modeling an HR system
# Employee models
from .contacts import AddressBook
from .hr import CommissionPolicy, HourlyPolicy, PayrollSystem, SalaryPolicy
from .productivity import (
    FactoryRole,
    ManagerRole,
    ProductivitySystem,
    SalesRole,
    SecretaryRole,
)

# class PayrollSystem:
#     def calculate_payroll(self, employees):
#         print('Calculating Payroll')
#         print('___________________')
#         for employee in employees:
#             print(f'Payroll for: {employee.id} - {employee.name}')
#             print(f'- Check amount: {employee.calculate_payroll()}')
#             print('')


class EmployeeDatabase:
    '''
    Keeps track of all the employees in the company. It has an instance of
    the productivity_system, the payrollsystem and addresbook used to create employee.
    The .employee property returns the list of employees and the employee objects are created by an internal
    method ._create_employee().
    '''
    def __init__(self):
        self._employees = [
            {
                'id': 1,
                'name': 'Eunice Boakye', 
                'role': 'Manager'
            },
            {
                'id': 2,
                'name': 'Maxine Baddoo', 
                'role': 'secretary',
            },
            {
                'id': 3,
                'name': 'Baaba Aggrey', 
                'role': 'sales',
            },
            {
                'id': 4,
                'name': 'Esther Ahene', 
                'role': 'factory',
            },
            {
                'id': 5,
                'name': 'Harriet Opoku', 
                'role': 'secretary',
            },
        ]
        self.productivity = ProductivitySystem()
        self.payroll = PayrollSystem()
        self._employee_addresses = AddressBook()

    @property
    def employees(self):
        return [self._create_employee(**data) for data in self._employees]

    def _create_employee(self, id, name, role):
        address = self._employee_addresses.get_employee_address(id)
        employee_role = self.productivity.get_role(role)
        payroll_policy = self.payroll.get_policy(id)
        return Employee(id, name, address, employee_role, payroll_policy)


class Employee:
    '''
    Employee base class for modeling all employees types.
    '''
    def __init__(self, id, name, address, role, payroll):
        self.id = id
        self.name = name
        self.address = None
        self.address = address
        self.role = role
        self.payroll = payroll

    def work(self, hours):
        duties = self.role.perform_duties(hours)
        print(f'Employee {self.id} - {self.name}:')
        print(f'- {duties}')
        print('')
        self.payroll.track_work(hours)
    
    def calculate_payroll(self):
        return self.payroll.calculate_payroll()



class Manager(Employee, ManagerRole, SalaryPolicy):
    '''
    Permanent employees paid fixed salary weekly.
    '''
    def __init__(self, id, name, weekly_salary):
        SalaryPolicy.__init__(self, weekly_salary)
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
    '''
    Sales reps paid a fixed salary plus commission on sales.
    '''
    def __init__(self, id, name, weekly_salary, commission):
        CommissionPolicy.__init__(self, weekly_salary, commission)
        super().__init__(id, name)



class FactoryWorker(Employee, FactoryRole, HourlyPolicy):
    def __init__(self, id, name, hours_worked, hour_rate):
        HourlyPolicy.__init__(self, hours_worked, hour_rate)
        super().__init__(id, name)


class TemporarySecretary(Employee, SecretaryRole, HourlyPolicy):
    '''
    Temporary workers.
    '''
    def __init__(self, id, name, hours_worked, hour_rate):
        HourlyPolicy.__init__(self, hours_worked, hour_rate)
        super().__init__(id, name)

