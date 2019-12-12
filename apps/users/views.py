# coding:utf-8
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.serializers import UserInfoSerializer

# Create your views here.
from utils.constants import Constants


class UserView(APIView):
    """
    用户新增
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request):
        """
        用户列表查询
        :param request:
        :return:
        """
        result = {"content": [], "totalElements": 0}
        return Response(data=result, status=Constants.HTTP_200_CODE)

    def post(self, request):
        """
        用户新增
        :param request:
        :return:
        """
        req_data = request.data  # {"username":'', "password":''}
        user = User.objects.create_superuser(username='用户名', password='密码', email='邮箱')
        user = User.objects.create_user(username='用户名', password='密码', email='邮箱')
        result = {}
        return Response(data=result, status=Constants.HTTP_200_CODE)

    def put(self, request):
        """
        用户信息修改
        :param request:
        :return:
        """
        return Response(status=Constants.HTTP_200_CODE)

    def delete(self, request):
        """
        删除用户
        :param request:
        :return:
        """
        return Response(status=Constants.HTTP_200_CODE)


class UserInfoView(APIView):
    """
    用户信息
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request):
        result = {"id": 1, "is_superuser": True, "username": "root", "email": "", "is_staff": True, "is_active": True,
                  "date_joined": "2019-11-26T04:25:37.348915Z", "is_staff_value": "具有管理后台权限", "is_active_value": "激活",
                  "roles": ["dept:edit", "user:list", "storage:add", "redis:list", "dept:add", "storage:edit",
                            "menu:del", "roles:del", "admin", "storage:list", "job:edit", "user:del", "dict:add",
                            "redis:del", "dept:list", "timing:add", "job:list", "dict:del", "dict:list", "job:add",
                            "timing:list", "roles:add", "user:add", "pictures:list", "menu:edit", "timing:edit",
                            "menu:list", "storage:del", "roles:list", "pictures:del", "menu:add", "job:del",
                            "pictures:add", "user:edit", "roles:edit", "timing:del", "dict:edit", "dept:del"]}
        return Response(data=result, status=Constants.HTTP_200_CODE)
