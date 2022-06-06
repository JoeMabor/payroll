
from apps.core.services import get_tax_bracket_by_amount
from apps.employees.services import get_employees, get_employees_by_ids
from ..services import add_payroll, get_payroll_by_id, add_pay
from .data_models import SavePayData
from ..domain.data_models import NetPayCalcData
from ..domain.salary.net_pay import NetPayCalculator


class PayrollRunner:

    def _calculate_empl_net_pay(self, payroll_id: int, empl) -> SavePayData:
        gross_pay = empl.salary
        tax_b = get_tax_bracket_by_amount(gross_pay)
        data = NetPayCalcData(
            basic_salary=empl.salary, tax_rate=tax_b.rate_ratio
        )

        n_calc = NetPayCalculator(data)
        result = n_calc.calculate_net_pay()
        print(f"payroll id:- '{payroll_id}'")

        data = SavePayData(
            payroll_id=payroll_id,
            empl_id=empl.id,
            gross_pay=gross_pay,
            net_pay=result.net_pay,
            tax_amount=result.tax,
            tax_bracket_id=tax_b.id
        )
        return data

    def _pay_employees(self,payroll_id, empls):
        pays = []
        for empl in empls:
            data = self._calculate_empl_net_pay(payroll_id,empl)
            pay = add_pay(data)
            pays.append(pay)
        return pays

    def run(self, pay=False):
        payroll = add_payroll()
        pays = []
        if pay:
            print("Running employees payroll")
            pays = self.pay_employees(payroll_id=payroll.id)

        return payroll, pays

    def pay_employees(self, payroll_id, empl_ids: list=None):
        """Pay employees of given IDS. If empl_ids is None, all employees in a company are paid"""
        if empl_ids is None:
            empls = get_employees()
        else:
            empls = get_employees_by_ids(empl_ids)
        return self._pay_employees(payroll_id=payroll_id, empls=empls)

