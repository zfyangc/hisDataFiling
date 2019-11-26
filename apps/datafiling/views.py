from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView


# 归档记录相关接口
class HisRecordListView(APIView):
    """归档历史记录列表"""
    def get(self):
        pass

class UpdateHisRecordView(APIView):

    def put(self):
        pass

# 归档操作接口
class FilingHisRecordView(APIView):
    """执行归档操作"""
    def post(self):
        pass


# 策略相关接口
class StrategyListView(APIView):
    def get(self):
        pass


class AddStrategyView(APIView):
    def post(self):
        pass


class UpdateStrategyView(APIView):
    def pust(self):
        pass

class DeleteStrategyView(APIView):
    def post(self):
        pass
