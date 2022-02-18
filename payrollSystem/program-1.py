from . import hr
from . import disgruntled

salary_employee = hr.SalaryEmployee(1, 'Maxine Baddoo', 1500)
hourly_employee = hr.HourlyEmployee(2, 'Eunice Boakye', 40, 15)
commission_employee = hr.CommissionEmployee(3, 'Baaba Aggrey', 1000, 250)
disgruntled_employee = disgruntled.DisgruntledEmployee(20_000, 'Anonymous')
payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee,
    disgruntled_employee,
])