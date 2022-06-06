from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from apps.core.api.views import TaxBracketViewSet
from apps.employees.api.views import EmployeesViewSet, DepartmentViewSet, DesignationViewSet
from apps.payroll.api.views import PayrollViewSet, PayViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# employees app
router.register(r"employees", EmployeesViewSet, basename="employee")
router.register(r"departments", DepartmentViewSet, basename="department")
router.register(r"designations", DesignationViewSet, basename="designation")

# run App
router.register(r"tax-brackets", TaxBracketViewSet, basename="tax-bracket")
router.register(r"payrolls", PayrollViewSet, basename="payroll")
router.register(r"pays", PayViewSet, basename="pay")

app_name = "api"
urlpatterns = router.urls
