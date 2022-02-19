# OOP
# Driver code
from . import employee
from . import productivity
from . import hr

salary_employee = employee.SalaryEmployee(1, 'Maxine Baddoo', 1500)
hourly_employee = employee.HourlyEmployee(2, 'Eunice Boakye', 40, 15)
commission_employee = employee.CommissionEmployee(3, 'Baaba Aggrey', 1000, 250)
factory_worker = employee.FactoryWorker(5, 'Jamila Brown', 40, 15)
temporary_secretary = employee.TemporarySecretary(6, 'Loretta Aggrey', 40, 9)
payroll_system = employee.PayrollSystem()
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee,
    temporary_secretary,
])


productivity_system = productivity.ProductivitySystem()
productivity_system.track(employee, 40)
payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(employee)


