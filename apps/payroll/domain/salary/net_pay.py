"""
Contains domain for NetPay that should include calculations of NetPay
"""
from ...domain.data_models import (
    NetPayCalcData,
    NetPayCalcResultData,
)


class NetPayCalculator:
    """Calculates employee NetPays"""

    def __init__(self, net_pay_data: NetPayCalcData):
        self._net_pay_data = net_pay_data

    def _calculate_gross_pay(self):
        return self._net_pay_data.basic_salary + self._net_pay_data.total_allowances

    def _calculate_tax(self, gross_salary):
        return gross_salary * self._net_pay_data.tax_rate

    def calculate_net_pay(self):
        """Calculate Employee NetPay"""
        gross_salary = self._calculate_gross_pay()
        tax = self._calculate_tax(gross_salary)
        net_pay = gross_salary - tax - self._net_pay_data.total_deductions
        return NetPayCalcResultData(net_pay, tax)
