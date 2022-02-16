# OOP 
# Modeling an HR system

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


class HourlyEmployee(Employee):
    '''
    Derived class from employee.
    '''
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate

    
