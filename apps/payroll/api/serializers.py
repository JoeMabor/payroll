from rest_framework import serializers

from ..models import Pay, Payroll
from ..use_cases.data_models import PayStatus


class PayOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pay

        fields = "__all__"
        read_only_fields = [
            "created_at",
            "updated",
            "gross_pay",
            "net_pay",
            "tax_bracket",
            "tax_amount",
        ]


class PayInputSerializer(serializers.Serializer):
    payroll = serializers.IntegerField(required=True)
    created_at = serializers.DateTimeField(required=False)
    employees = serializers.ListField(required=True)


class PayUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    status = serializers.ChoiceField(required=True, choices=PayStatus.statuses())


class PayrollOutputSerializer(serializers.ModelSerializer):
    pays = PayOutputSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Payroll
        fields = "__all__"


class PayrollInputSerializer(serializers.Serializer):
    calendar = serializers.CharField(max_length=9, required=False)
    begin_at = serializers.DateTimeField(required=False)
    end_at = serializers.DateTimeField(required=False)
    pay = serializers.BooleanField(default=False)
