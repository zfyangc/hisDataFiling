# coding:utf-8
import json
import traceback

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user.serializers import UserInfoSerializer

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
        code_str = req_data.get('code', '')
        code_uuid = req_data.get('uuid', '')
        result = {}
        # user = auth.authenticate(username=username, password=password)
        # if user is None:
        #     result['resullt'] = 'fail'
        #     result['message'] = '此用户不存在'
        #     return Response(data=result, status=Constants.HTTP_400_CODE)
        # if not user.is_active:
        #     result['resullt'] = 'fail'
        #     result['message'] = '用户未激活'
        #     return Response(data=result, status=Constants.HTTP_400_CODE)
        # 清除验证码
        try:
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
            user_token = Token.objects.get(user=user)
            if user_token:
                user_token.delete()
                user_token, _ = Token.objects.get_or_create(user=user)
            try:
                result['token'] = user_token.key
                result['user'] = UserInfoSerializer(user).data
                result['user']['roles'] = ["dept:edit", "user:list", "storage:add", "redis:list", "dept:add", "storage:edit",
                                   "menu:del", "roles:del", "admin", "storage:list", "job:edit", "user:del", "dict:add",
                                   "redis:del", "dept:list", "timing:add", "job:list", "dict:del", "dict:list",
                                   "job:add", "timing:list", "roles:add", "user:add", "pictures:list", "menu:edit",
                                   "timing:edit", "menu:list", "storage:del", "roles:list", "pictures:del", "menu:add",
                                   "job:del", "pictures:add", "user:edit", "roles:edit", "timing:del", "dict:edit",
                                   "dept:del"]
                result['resullt'] = 'success'
                result['message'] = '登录成功'
                return Response(data=result, status=Constants.HTTP_200_CODE)
            except Exception:
                traceback.print_exc()
                result['resullt'] = 'fail'
                result['message'] = '用户权限认证失败'
                return Response(data=result, status=Constants.HTTP_401_CODE)
        except Exception as e:
            traceback.print_exc()
            result = {'result': 'fail', 'message': e}
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
        img_str = type + vcm.generateCodeImg()
        codeRes = vcm.getCodeResult()
        uuid_str = 'code_key' + str(uuid.uuid1())[:8] + str(uuid.uuid4())[8:]
        json.dumps(codeRes)
        CacheManager.save(uuid_str, codeRes)
        return Response(data=ImageResult(img_str, uuid_str).__dict__, status=Constants.HTTP_200_CODE)
