from django.contrib import admin

from aqis.models import Aqi


@admin.register(Aqi)
class AqiAdmin(admin.ModelAdmin):
    list_display = (
        'city',
        'pm25_value',
        'pm25_level',
        'datetime',
    )
    list_filter = (
        'city',
        'pm25_value',
        'pm25_level',
        'datetime',
    )
    search_fields = [
        'city',
        'pm25_value',
        'pm25_level',
        'datetime',
    ]
