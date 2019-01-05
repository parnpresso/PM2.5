from django.contrib import admin

from aqis.models import Aqi

@admin.register(Aqi)
class AqiAdmin(admin.ModelAdmin):
    list_display = ('city', 'pm_value', 'pm_level', 'datetime')
    list_filter = ('city', 'pm_value', 'pm_level', 'datetime')
    search_fields = ['city', 'pm_value', 'pm_level', 'datetime']
