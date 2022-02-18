# OOP 
# Modeling an HR system
# Employee models

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

    def calculate_payroll(self):
        return self.weekly_salary


class SalaryEmployee(Employee):
    '''
    Permanent employees paid fixed salary weekly.
    '''
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary


class HourlyEmployee(Employee):
    '''
    Derived class from employee.
    Employees paid by the hour.
    '''
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


class CommissionEmployee(SalaryEmployee):
    '''
    Sales reps paid a fixed salary plus commission on sales.
    '''
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission
    
    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission
