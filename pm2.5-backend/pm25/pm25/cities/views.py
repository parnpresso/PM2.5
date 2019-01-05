from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView




class CityListView(APIView):
    def get(self, request):
        # poppers = Popper.objects.all().values(
        #     'user',
        #     'popper_type',
        #     'popper_facebook',
        #     'popper_line',
        #     'is_actived',
        # )

        # data = list(poppers)

        data = {
            'city': 'Bangkok',
            'pm_value': 112,
            'pm_level': 6,
            'date': '2019-01-05 19:00:00',
        }

        return Response(data, status=status.HTTP_200_OK)
