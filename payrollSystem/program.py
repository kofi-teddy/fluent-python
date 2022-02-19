# OOP
# Driver code
from . import employees
from . import productivity
from . import hr
from . import contacts

# salary_employee = employee.SalaryEmployee(1, 'Maxine Baddoo', 1500)
# hourly_employee = employee.HourlyEmployee(2, 'Eunice Boakye', 40, 15)
# commission_employee = employee.CommissionEmployee(3, 'Baaba Aggrey', 1000, 250)
# factory_worker = employee.FactoryWorker(5, 'Jamila Brown', 40, 15)
# temporary_secretary = employee.TemporarySecretary(6, 'Loretta Aggrey', 40, 9)
# # payroll_system = employee.PayrollSystem()
# # payroll_system.calculate_payroll([
# #     salary_employee,
# #     hourly_employee,
# #     commission_employee,
# #     temporary_secretary,
# # ])

manager = employees.Manager(1, 'Eunice Boakye', 3000)
manager.address = contacts.Address(
    'Adenta area',
    'Accra',
    'Ad',
    '2233'
)
secretary = employees.Secretary(2, 'Baaba Aggrey', 1500)
secretary.address = contacts.Address(
    'Eastlegon',
    'Lakeside',
    'Bd',
    '2233'
)
sales_guy = employees.SalesPerson(3, 'Maxine Baddoo', 1000, 250)
factory_worker = employees.FactoryWorker(4, 'Esther Ahene', 40, 15)
temporary_secretary = employees.TemporarySecretary(5, 'Kuukua Charlotte', 40, 9)

employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
    temporary_secretary,
] 

productivity_system = productivity.ProductivitySystem()
productivity_system.track(employees, 40)
payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(employees)


