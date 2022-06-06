from django.db import models

from apps.core.models import Address, TimestampModel


class Department(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(max_length=250, null=True)

    def __str__(self):
        return self.name


class Designation(models.Model):
    name = models.CharField(max_length=250, unique=True)
    function = models.CharField(max_length=250, null=True)
    description = models.TextField(max_length=250, null=True)

    def __str__(self):
        return self.name


class PayTypes:
    """Define supported Employee types"""

    SALARY = 1
    HOURLY = 2


class EmployeeTypes:
    FULL_TIME = 1
    PART_TIME = 2


class Employee(TimestampModel):
    EMPLOYEE_TYPES = (
        (EmployeeTypes.FULL_TIME, "Full time"),
        (EmployeeTypes.PART_TIME, "Part time"),
    )

    PAY_TYPES = [
        (PayTypes.SALARY, "Salary"),
        (PayTypes.HOURLY, "Hourly"),
    ]
    GENDERS = [("M", "Male"), ("F", "Female")]
    employee_id = models.CharField(unique=True, max_length=10)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDERS)
    dob = models.DateField(verbose_name="D.O.B", null=True)

    employee_type = models.IntegerField(
        choices=EMPLOYEE_TYPES, default=EmployeeTypes.FULL_TIME
    )
    pay_type = models.IntegerField(choices=PAY_TYPES, default=PayTypes.SALARY)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    salary = models.DecimalField(
        max_digits=12, decimal_places=2, null=True
    )  # Gross Basic/Base Salary
    hourly_rate = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    join_date = models.DateField(auto_now_add=True)

    @property
    def is_salaried(self):
        return self.pay_type == PayTypes.SALARY

    @property
    def is_paid_hourly(self):
        return self.pay_type == PayTypes.HOURLY

    def __str__(self):
        return f"{self.first_name} {self.surname}"


class Allowance(TimestampModel):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=250, null=True, blank=True)
    is_percent = models.BooleanField(default=True)
    value = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name


class EmployeeAllowance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    allowance = models.ForeignKey(Allowance, on_delete=models.CASCADE)
    remark = models.TextField(max_length=250, null=True, blank=True)

    class Meta:
        unique_together = ("employee", "allowance")


class Deduction(TimestampModel):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=250, null=True, blank=True)
    is_percent = models.BooleanField(default=False)
    value = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name


class EmployeeDeduction(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    deduction = models.ForeignKey(Deduction, on_delete=models.CASCADE)
    remarks = models.TextField(max_length=250, null=True, blank=True)
