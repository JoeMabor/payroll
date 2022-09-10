from dataclasses import dataclass
from decimal import Decimal


class PayrollStatus:
    DRAFT = "DRAFT"
    APPROVED = "APPROVED"


class PayStatus:
    NOT_PAID = "NOT_PAID"
    PAID = "PAID"

    @classmethod
    def statuses(cls):
        return (
            (cls.NOT_PAID, "Not Paid"),
            (cls.PAID, "Paid")
        )


class Calendar:
    """Pay Calender"""

    MONTHLY = "MONTHLY"
    WEEKLY = "WEEKLY"
    BI_WEEKLY = "BI_WEEKLY"


@dataclass
class SavePayData:
    payroll_id: int
    empl_id: int
    basic_salary: Decimal
    total_allowance: Decimal
    total_deduction: Decimal
    gross_pay: Decimal
    net_pay: Decimal
    tax_bracket_id: int
    tax_amount: Decimal
    status: str = PayStatus.NOT_PAID
    empl_allowances: list = None
