# coding:utf-8
import traceback

from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

from utils.auth import ExpiringTokenAuthentication

# Create your views here.
from utils.cache_manager import CacheManager
from utils.constants import Constants
from utils.validcode_manager import ValidCodeManager, ImageResult
import uuid


class LoginView(APIView):
    """
    用户登录
    """
    serializer_class = AuthTokenSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def post(self, request):
        req_data = request.data  # {"username":'', "password":''}
        username = req_data.get('username', '')
        password = req_data.get('password', '')
        code_str = req_data.get('code', '')
        code_uuid = req_data.get('uuid', '')
        result = {}
        user_instance = User.objects.filter(username=username).first()
        if user_instance:
            if user_instance.password != password:
                result['resullt'] = 'fail'
                result['message'] = '密码错误'
                return Response(data=result, status=Constants.HTTP_400_CODE)
            code = CacheManager.get(code_uuid)
            CacheManager.delete(code_uuid)
            if not code:
                result['resullt'] = 'fail'
                result['message'] = '验证码已过期'
                return Response(data=result, status=Constants.HTTP_400_CODE)
            if code_str != '' and code_str != code:
                result['resullt'] = 'fail'
                result['message'] = '验证码错误'
                return Response(data=result, status=Constants.HTTP_400_CODE)

            serializer = self.serializer_class(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            _, _ = Token.objects.get_or_create(user=user)
            try:
                aa = ExpiringTokenAuthentication()
                _, token = aa.authenticate(request)
                result['token'] = token
                result['resullt'] = 'success'
                result['message'] = '登录成功'
                return Response(data=result, status=Constants.HTTP_200_CODE)
            except Exception:
                traceback.print_exc()
                result['resullt'] = 'fail'
                result['message'] = '用户权限认证失败'
                return Response(data=result, status=Constants.HTTP_401_CODE)
        else:
            result = {'result': 'fail', 'message': "此用户不存在"}
            return Response(data=result, status=Constants.HTTP_400_CODE)


class LogoutView(APIView):
    """
    用户登出
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def delete(self, request):
        pass


class UserInfoView(APIView):
    """
    用户信息
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self):
        pass


class ValidCodeInfoView(APIView):
    """
    图形检验码
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request):
        vcm = ValidCodeManager(111, 36)
        type = 'data:image/png;base64,'
        img_str = type+vcm.generateCodeImg()
        codeRes = vcm.getCodeResult()
        uuid_str = 'code_key' + str(uuid.uuid1())[:8] + str(uuid.uuid4())[8:]
        CacheManager.save(uuid_str, str(codeRes))
        return Response(data=ImageResult(img_str, uuid_str).__dict__, status=Constants.HTTP_200_CODE)
