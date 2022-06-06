from django.contrib import admin

from .models import Employee, Allowance, Deduction

admin.site.register(Employee)
admin.site.register(Allowance)
admin.site.register(Deduction)