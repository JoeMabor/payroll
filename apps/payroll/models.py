import calendar
import datetime

from django.db import models

from apps.core.models import TimestampModel, TaxBracket
from apps.employees.models import Employee, EmployeeAllowance, EmployeeDeduction
from .use_cases.data_models import Calendar, PayrollStatus, PayStatus

today = datetime.datetime.now()
month_first_weekday, month_last_day = calendar.monthrange(today.year, today.month)


class Payroll(TimestampModel):
    """Model for Payroll"""

    STATUSES = (
        (PayrollStatus.DRAFT, "Draft"),
        (PayrollStatus.APPROVED, "Approved"),
    )

    CALENDARS = (
        (Calendar.MONTHLY, "Monthly"),
        (Calendar.WEEKLY, "Weekly"),
        (Calendar.BI_WEEKLY, "Bi-Weekly"),
    )
    calendar = models.CharField(
        max_length=10, choices=CALENDARS, default=Calendar.MONTHLY
    )
    begin_at = models.DateField(
        default=datetime.date(year=today.year, month=today.month, day=1)
    )
    end_at = models.DateField(
        default=datetime.date(year=today.year, month=today.month, day=month_last_day)
    )
    status = models.CharField(max_length=10, choices=PayrollStatus.statuses(), default=PayrollStatus.DRAFT)


class Pay(TimestampModel):
    payroll = models.ForeignKey(Payroll, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=PayStatus.statuses(), default=PayStatus.NOT_PAID)
    basic_salary = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    total_allowance = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    total_deduction = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    gross_pay = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    net_pay = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    tax_bracket = models.ForeignKey(TaxBracket, on_delete=models.CASCADE, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    allowances = models.ManyToManyField(EmployeeAllowance)
    deductions = models.ManyToManyField(EmployeeDeduction)

    class Meta:
        unique_together = ("payroll", "employee")