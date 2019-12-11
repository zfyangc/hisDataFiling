# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from utils.constants import Constants


class LogDownloadView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request):
        return Response(status=Constants.HTTP_200_CODE)
class LogInfoView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request):
        return Response(status=Constants.HTTP_200_CODE)

class UserLogInfoView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request):
        return Response(status=Constants.HTTP_200_CODE)

class ErrorLogInfoView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request):
        key = request.GET.get('key', '')
        return Response(status=Constants.HTTP_200_CODE)

