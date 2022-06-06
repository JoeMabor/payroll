from .models import TaxBracket


def get_tax_bracket_by_amount(amount):
    return TaxBracket.objects.get_tax_bracket_by_amount(amount)
