from django.urls import path

from cities.views import CityListView


urlpatterns = [
    path('', CityListView.as_view(), name='city_list'),
]
