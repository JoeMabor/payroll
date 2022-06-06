from decimal import Decimal

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Country(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return f"{self.name}"


class State(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class City(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return f"{self.name}"


class Address(TimestampModel):
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, null=True)
    post_code = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


class TaxBracketManager(models.Manager):
    """Model manager for Tax brackets"""

    def get_tax_bracket_by_amount(self, amount):

        objs = self.all()
        for obj in objs:
            if obj.min_limit <= amount <= obj.max_limit:
                return obj


class TaxBracket(TimestampModel):
    """Tax brackets"""
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    min_limit = models.FloatField()
    max_limit = models.FloatField()
    rate_percent = models.IntegerField(
        verbose_name="Tax Rate",
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    active = models.BooleanField(default=True)  # If it is used currently

    @property
    def rate_ratio(self):
        return Decimal(round(self.rate_percent / 100, 2))

    objects = TaxBracketManager()
