from django.contrib import admin

from search.models import (
    Car,
    Manufacturer,
)


admin.site.register(Car)
admin.site.register(Manufacturer)