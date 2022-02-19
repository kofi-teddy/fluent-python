# Productivity app

class ProductivitySystem:
    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('______________________________')
        for employee in employees:
            employee.work(hours)
        print('')


class ManagerRole:
    def work(self, hours):
        print(f'{self.name} screams and yells for {hours} hours.')


class SecretaryRole:
    def work(self, hours):
        print(f'{self.name} expends {hours} hours doing office paperwork.')


class SalesRole:
    def work(self, hours):
        print(f'{self.name} expends {hours} on the phone.')


class FactoryRole:
    def work(self, hours):
        print(f'{self.name} manufactures gadgets for {hours} hours.')

