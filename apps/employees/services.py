from .models import Employee


def get_employees():
    return Employee.objects.all()


def get_employees_by_ids(empl_ids: list):
    return Employee.objects.filter(pk__in=empl_ids)
