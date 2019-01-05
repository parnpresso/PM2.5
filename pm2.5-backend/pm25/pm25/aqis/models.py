from django.db import models

from cities.models import City

class Aqi(models.Model):
    city = models.ForeignKey(
        City,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    pm25_value = models.CharField(max_length=100)
    pm25_level = models.CharField(max_length=100)
    datetime = models.CharField(max_length=100)
