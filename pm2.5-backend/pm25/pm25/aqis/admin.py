from django.contrib import admin

from aqis.models import Aqi


@admin.register(Aqi)
class AqiAdmin(admin.ModelAdmin):
    list_display = (
        'city',
        'datetime'
    )
    list_filter = (
        'city',
        'datetime'
    )
    search_fields = [
        'city',
        'datetime'
    ]
