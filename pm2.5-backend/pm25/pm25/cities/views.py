from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from aqis.models import Aqi
from cities.models import City


class CityListView(APIView):
    def get(self, request):
        city = City.objects.get(name='Bangkok')
        aqi = Aqi.objects.filter(city=city).order_by('pk')

        data = {
            'city': city.name,
            'pm_value': aqi[0].pm25_value,
            'pm_level': aqi[0].pm25_level,
            'date': aqi[0].datetime,
        }

        return Response(data, status=status.HTTP_200_OK)
