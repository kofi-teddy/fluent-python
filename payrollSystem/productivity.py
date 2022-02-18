# Productivity app

class ProductivitySystem:
    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('______________________________')
        for employee in employees:
            employee.workd(hours)
        print('')