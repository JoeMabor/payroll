from django.contrib import admin

from .models import Employee, Allowance, Deduction, EmployeeAllowance, EmployeeDeduction

admin.site.register(Employee)
admin.site.register(Allowance)
admin.site.register(Deduction)
admin.site.register(EmployeeAllowance)
admin.site.register(EmployeeDeduction)