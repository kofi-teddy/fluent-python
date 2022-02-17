# OOP
# Driver code
import . hr

salary_employee = hr.SalaryEmployee(1, 'Maxine Baddoo', 1500)
hourly_employee = hr.HourlyEmployee(2, 'Eunice Boakye', 40, 15)
commission_employee = hr.CommissionEmployee(3, 'Baaba Aggrey', 1000, 250)
payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee,
])

