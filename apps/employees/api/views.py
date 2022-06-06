from rest_framework.viewsets import ModelViewSet

from ..models import Department, Designation, Employee
from .serializers import DepartmentSerializer, DesignationSerializer, EmployeeSerializer


class EmployeesViewSet(ModelViewSet):
    """A View set for  employees"""

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class DepartmentViewSet(ModelViewSet):
    """A View set for departments"""

    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class DesignationViewSet(ModelViewSet):
    """A View set for designations"""

    serializer_class = DesignationSerializer
    queryset = Designation.objects.all()
