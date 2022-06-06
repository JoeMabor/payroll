from rest_framework import serializers

from ..models import Department, Designation, Employee, PayTypes


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:

        model = Employee
        fields = [
            "id",
            "employee_id",
            "first_name",
            "surname",
            "gender",
            "dob",
            "employee_type",
            "pay_type",
            "department",
            "designation",
            "address",
            "salary",
            "hourly_rate",
            "join_date",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated"]

    UPDATABLE_FIELDS = [
        "first_name",
        "surname",
        "gender",
        "dob",
        "employee_type",
        "pay_type",
        "department",
        "designation",
        "address",
        "salary",
        "hourly_rate",
        "join_date",
    ]

    def _is_attribute_available(self, data, attr):
        return attr in data and data[attr]

    def _check_pay_attribute(self, data: dict):
        if data["pay_type"]:
            pay_type = data["pay_type"]
            if pay_type == PayTypes.SALARY:
                # Check that Salary is provided
                if not self._is_attribute_available(data, "salary"):
                    raise serializers.ValidationError(
                        "'salary' must be provided for salary paid employee."
                    )
            elif pay_type == PayTypes.HOURLY:
                if not self._is_attribute_available(data, "hourly_rate"):
                    raise serializers.ValidationError(
                        "'hourly_rate' must be provided for hourly paid employee."
                    )
            else:
                raise serializers.ValidationError(
                    f"Unrecognized  employee Pay Type'{pay_type}'"
                )

    def validate(self, data):
        """Add custom validations"""
        self._check_pay_attribute(data)
        # TODO: Check during update that salary field is updated for salary employee and same for hourly employee
        return data


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = "__all__"
