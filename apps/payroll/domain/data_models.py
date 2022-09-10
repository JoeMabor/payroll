""" Data models
Contain defined data structures and classes.

"""
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class NetPayCalcData:
    """Data structure for Net Pay calculation request data"""

    basic_salary: float
    tax_rate: float
    total_allowances: float = 0
    total_deductions: float = 0


@dataclass
class NetPayCalcResultData:
    """Data structure for Net Pay calculation results"""
    net_pay: Decimal
    tax: Decimal
