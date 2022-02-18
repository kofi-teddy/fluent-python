'''
A class that does not inherit from the employee
base class.
'''

class DisgruntledEmployee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def calculate_payroll(self):
        return 1_000_000

