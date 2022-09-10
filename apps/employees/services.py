from .models import Employee, EmployeeAllowance


def get_employees():
    return Employee.objects.all()


def get_employees_by_ids(empl_ids: list):
    return Employee.objects.filter(pk__in=empl_ids)


def get_employee_allowances(empl_id):
    return EmployeeAllowance.objects.filter(employee_id=empl_id)
