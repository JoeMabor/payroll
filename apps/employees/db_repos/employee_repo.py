from ..models import Employee


class EmployeeRepo:

    def get_by_id(self, id_):
        return Employee.objects.get(pk=id_)
