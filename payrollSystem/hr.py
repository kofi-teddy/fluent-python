# OOP 
# Modeling an HR system

class PayrollSystem:
    def __init__(self):
        self_employee_policies = {
            1: SalaryPolicy(3000),
            2: SalaryPolicy(1500),
            3: CommissionPolicy(1000, 100),
            4: HourlyPolicy(15),
            5: HourlyPolicy(9)
        }

    

    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('___________________')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')
            if employee.address:
                print('-Sent to:')
                print(employee.address)
            print('')


class SalaryPolicy:
    '''
    Permanent employees paid fixed salary weekly.
    '''
    def __init__(self, weekly_salary):
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyPolicy:
    '''
    Derived class from employee.
    Employees paid by the hour.
    '''
    def __init__(self, hours_worked, hour_rate):
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


class CommissionPolicy(SalaryPolicy):
    '''
    Sales reps paid a fixed salary plus commission on sales.
    '''
    def __init__(self, weekly_salary, commission):
        super().__init__(weekly_salary)
        self.commission = commission
    
    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission

    
