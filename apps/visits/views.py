from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from utils.constants import Constants


class VisitsView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request):
        return Response(data={"newVisits": 2, "newIp": 1, "recentVisits": 10, "recentIp": 5},
                        status=Constants.HTTP_200_CODE)

    def post(self, request):
        return Response(status=Constants.HTTP_200_CODE)


class CharDataInfoView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request):
        return Response(data={"weekDays": ["Wed", "Thu", "Fri", "Mon", "Tue"], "ipData": [1, 1, 1, 1, 1],
                              "visitsData": [3, 3, 1, 1, 2]}, status=Constants.HTTP_200_CODE)
