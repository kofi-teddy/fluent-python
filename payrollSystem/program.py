# OOP
# Driver code
from . import employee

salary_employee = employee.SalaryEmployee(1, 'Maxine Baddoo', 1500)
hourly_employee = employee.HourlyEmployee(2, 'Eunice Boakye', 40, 15)
commission_employee = employee.CommissionEmployee(3, 'Baaba Aggrey', 1000, 250)
payroll_system = employee.PayrollSystem()
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee,
])

