from django.contrib import admin

from .models import Address, City, Country, State

admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Address)
