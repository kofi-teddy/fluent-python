#  Modeling an HR system

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
    Employee base class for modeling all employees types
    '''
    def __init__(self, id, name):
        self.id = id
        self.name = name

    
