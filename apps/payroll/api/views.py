from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from ..api.serializers import (
    PayOutputSerializer,
    PayrollOutputSerializer,
    PayrollInputSerializer, PayInputSerializer, PayUpdateSerializer
)
from ..services import get_payrolls, get_payroll_by_id, get_pays, get_pay_by_id, get_pays_by_payroll, update_pay
from ..use_cases.run_payroll import PayrollRunner


class PayrollViewSet(ViewSet):
    """A View set for  Pay Run"""

    payroll_runner = PayrollRunner()

    def list(self, request):
        objs = get_payrolls()
        serializer = PayrollOutputSerializer(objs, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PayrollInputSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            pay = data["pay"]
            payroll, pays = self.payroll_runner.run(pay=pay)
            setattr(payroll, "pays", pays)
            output = PayrollOutputSerializer(payroll)
            return Response(output.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        obj = get_payroll_by_id(pk)
        pays = get_pays_by_payroll(pk)
        setattr(obj, "pays", pays)
        serializer = PayrollOutputSerializer(obj)

        return Response(serializer.data)

    def update(self):
        pass


class PayViewSet(ViewSet):
    """A View set for an employee Pay"""
    payroll_runner = PayrollRunner()

    def list(self, request):
        payroll_id = request.GET.get("payroll")
        employee_id = request.GET.get("employee")
        objs = get_pays(payroll_id, employee_id)
        serializer = PayOutputSerializer(objs, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PayInputSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            pays = self.payroll_runner.pay_employees(payroll_id=data["payroll"], empl_ids=data["employees"])
            serializer = PayOutputSerializer(pays, many=True)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        obj = get_pay_by_id(pk)
        serializer = PayOutputSerializer(obj)

        return Response(serializer.data)

    def update(self, request, pk=None):
        serializer = PayUpdateSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            obj = update_pay(data["id"], data["status"])
            serializer = PayOutputSerializer(obj)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


