from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from utils.constants import Constants


class MenuDownloadView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request):
        pass


class MenuBuildView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request):
        result = [{"name": "系统管理", "path": "/system", "hidden": False, "redirect": "noredirect", "component": "Layout",
                   "alwaysShow": True, "meta": {"title": "系统管理", "icon": "system", "noCache": True}, "children": [
                {"name": "User", "path": "user", "hidden": False, "component": "system/user/index",
                 "meta": {"title": "用户管理", "icon": "peoples", "noCache": True}},
                {"name": "Role", "path": "role", "hidden": False, "component": "system/role/index",
                 "meta": {"title": "角色管理", "icon": "role", "noCache": True}},
                {"name": "Menu", "path": "menu", "hidden": False, "component": "system/menu/index",
                 "meta": {"title": "菜单管理", "icon": "menu", "noCache": True}},
                {"name": "Dept", "path": "dept", "hidden": False, "component": "system/dept/index",
                 "meta": {"title": "部门管理", "icon": "dept", "noCache": True}},
                {"name": "Job", "path": "job", "hidden": False, "component": "system/job/index",
                 "meta": {"title": "岗位管理", "icon": "Steve-Jobs", "noCache": True}},
                {"name": "Dict", "path": "dict", "hidden": False, "component": "system/dict/index",
                 "meta": {"title": "字典管理", "icon": "dictionary", "noCache": True}}]},
                  {"name": "系统监控", "path": "/monitor", "hidden": False, "redirect": "noredirect", "component": "Layout",
                   "alwaysShow": True, "meta": {"title": "系统监控", "icon": "monitor", "noCache": True}, "children": [
                      {"name": "OnlineUser", "path": "online", "hidden": False, "component": "monitor/online/index",
                       "meta": {"title": "在线用户", "icon": "Steve-Jobs", "noCache": True}},
                      {"name": "Log", "path": "logs", "hidden": False, "component": "monitor/log/index",
                       "meta": {"title": "操作日志", "icon": "log", "noCache": True}},
                      {"name": "ErrorLog", "path": "errorLog", "hidden": False, "component": "monitor/log/errorLog",
                       "meta": {"title": "异常日志", "icon": "error", "noCache": True}},
                      {"name": "Redis", "path": "redis", "hidden": False, "component": "monitor/redis/index",
                       "meta": {"title": "系统缓存", "icon": "redis", "noCache": True}},
                      {"name": "Sql", "path": "druid", "hidden": False, "component": "monitor/sql/index",
                       "meta": {"title": "SQL监控", "icon": "sqlMonitor", "noCache": True}}]},
                  {"name": "系统工具", "path": "/sys-tools", "hidden": False, "redirect": "noredirect",
                   "component": "Layout", "alwaysShow": True,
                   "meta": {"title": "系统工具", "icon": "sys-tools", "noCache": True}, "children": [
                      {"name": "Timing", "path": "timing", "hidden": False, "component": "system/timing/index",
                       "meta": {"title": "定时任务", "icon": "timing", "noCache": True}},
                      {"name": "GeneratorIndex", "path": "generator", "hidden": False, "component": "generator/index",
                       "meta": {"title": "代码生成", "icon": "dev", "noCache": True}},
                      {"name": "Storage", "path": "storage", "hidden": False, "component": "tools/storage/index",
                       "meta": {"title": "存储管理", "icon": "qiniu", "noCache": True}},
                      {"name": "Email", "path": "email", "hidden": False, "component": "tools/email/index",
                       "meta": {"title": "邮件工具", "icon": "email", "noCache": True}},
                      {"name": "Pictures", "path": "pictures", "hidden": False, "component": "tools/picture/index",
                       "meta": {"title": "图床管理", "icon": "image", "noCache": True}},
                      {"name": "Swagger", "path": "swagger2", "hidden": False, "component": "tools/swagger/index",
                       "meta": {"title": "接口文档", "icon": "swagger", "noCache": True}},
                      {"name": "AliPay", "path": "aliPay", "hidden": False, "component": "tools/aliPay/index",
                       "meta": {"title": "支付宝工具", "icon": "alipay", "noCache": True}}]},
                  {"name": "组件管理", "path": "/components", "hidden": False, "redirect": "noredirect",
                   "component": "Layout", "alwaysShow": True,
                   "meta": {"title": "组件管理", "icon": "zujian", "noCache": True}, "children": [
                      {"name": "Icons", "path": "icon", "hidden": False, "component": "components/IconSelect",
                       "meta": {"title": "图标库", "icon": "icon", "noCache": True}},
                      {"name": "Editor", "path": "tinymce", "hidden": False, "component": "components/Editor",
                       "meta": {"title": "富文本", "icon": "fwb", "noCache": True}},
                      {"name": "Markdown", "path": "markdown", "hidden": False, "component": "components/MarkDown",
                       "meta": {"title": "Markdown", "icon": "markdown", "noCache": True}},
                      {"name": "YamlEdit", "path": "yaml", "hidden": False, "component": "components/YamlEdit",
                       "meta": {"title": "Yaml编辑器", "icon": "dev", "noCache": True}}]},
                  {"name": "多级菜单", "path": "/nested", "hidden": True, "redirect": "noredirect", "component": "Layout",
                   "alwaysShow": True, "meta": {"title": "多级菜单", "icon": "menu", "noCache": True}, "children": [
                      {"name": "二级菜单1", "path": "menu1", "hidden": False, "redirect": "noredirect",
                       "component": "nested/menu1/index", "alwaysShow": True,
                       "meta": {"title": "二级菜单1", "icon": "menu", "noCache": True}, "children": [
                          {"name": "三级菜单1", "path": "menu1-1", "hidden": False, "component": "nested/menu1/menu1-1",
                           "meta": {"title": "三级菜单1", "icon": "menu", "noCache": True}},
                          {"name": "三级菜单2", "path": "menu1-2", "hidden": False, "component": "nested/menu1/menu1-2",
                           "meta": {"title": "三级菜单2", "icon": "menu", "noCache": True}}]},
                      {"name": "二级菜单2", "path": "menu2", "hidden": False, "component": "nested/menu2/index",
                       "meta": {"title": "二级菜单2", "icon": "menu", "noCache": True}}]}]
        return Response(data=result, status=Constants.HTTP_200_CODE)


class MenuTreeView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request):
        pass
