import traceback

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from menu.models import Menu
from menu.serializers import MenuTreeSerializer, MenuBuildSerializer
from utils.auth import get_provider
from utils.constants import Constants


class MenuDownloadView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request):
        pass


class menuListView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        result = {}
        return Response(data=result, status=Constants.HTTP_200_CODE)


class MenuBuildView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_build_menu(self, menu_querySet):
        type = 2
        build_menu = menu_querySet.exclude(type=type)
        reuslt = []
        self.get_build_tree(build_menu, 0, reuslt)
        print(reuslt)

        return reuslt

    def get_build_tree(self, build_menu, pid, result):
        menu = build_menu.filter(pid=pid)
        if menu:
            serializer = MenuBuildSerializer(menu, many=True)
            for i in serializer.data:
                i["children"] = []
                id = i.pop("id")
                if i.get('component') == '':
                    i['component'] = 'Layout'
                type = i.pop('type')
                if type == 1:
                    _ = i.pop('redirect')
                    _ = i.pop('alwaysShow')
                result.append(i)
                self.get_build_tree(build_menu, id, i["children"])
        else:
            return

    def get(self, request):
        try:
            cur_user = get_provider(request)
            if cur_user:
                role = cur_user.role if cur_user.role else None
                menus = role.menu.all() if role else []
                result = self.get_build_menu(menus)
                return Response(data=result, status=Constants.HTTP_200_CODE)
            else:
                return Response(status=Constants.HTTP_401_CODE)
        except Exception:
            traceback.print_exc()
            return Response(status=Constants.HTTP_400_CODE)


class MenuTreeView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_menu_tree(self, result, pid):
        try:
            menus = Menu.objects.filter(pid=pid)
            if menus:
                serializer = MenuTreeSerializer(menus, many=True)
                for i in serializer.data:
                    i["children"] = []
                    result.append(i)
                    self.get_menu_tree(i["children"], i.get("id"))
            else:
                return
        except Exception:
            traceback.print_exc()
            return

    def get(self, request):
        result = []
        try:
            self.get_menu_tree(result, 0)
            print(result)
            return Response(data=result, status=Constants.HTTP_200_CODE)
        except Exception:
            traceback.print_exc()
            return Response(data=result, status=Constants.HTTP_400_CODE)
