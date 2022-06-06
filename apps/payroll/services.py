from .models import Payroll, Pay
from .use_cases.data_models import SavePayData


def get_payrolls():
    payrolls = Payroll.objects.all()

    return payrolls


def get_pays():
    return Pay.objects.all()


def get_payroll_by_id(id_):
    return Payroll.objects.get(pk=id_)


def get_pay_by_id(id_):
    return Pay.objects.get(pk=id_)


def get_pays_by_payroll(payroll_pk):
    return Pay.objects.filter(payroll_id=payroll_pk)


def add_pay(data: SavePayData):
    pay = Pay(
        payroll_id=data.payroll_id,
        employee_id=data.empl_id,
        status=data.status,
        gross_pay=data.gross_pay,
        net_pay=data.net_pay,
        tax_bracket_id=data.tax_bracket_id,
        tax_amount=data.tax_amount,
    )
    pay.save()
    return pay


def add_payroll():
    payroll = Payroll()
    payroll.save()
    return payroll


def update_pay(pay_id, status: str):
    obj = get_pay_by_id(pay_id)
    obj.status = status
    obj.save()
    return obj
