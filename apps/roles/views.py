from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from utils.constants import Constants


class RoleInfoView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        """

        :param request:
        :return:
        """
        result = {"content": [
            {"id": 1, "name": "超级管理员", "dataScope": "全部", "level": 1, "remark": "-", "permission": "admin", "menus": [
                {"id": 46, "type": 2, "permission": "user:del", "name": "用户删除", "sort": 4, "path": "", "component": "",
                 "pid": 2, "cache": False, "hidden": False, "componentName": "", "icon": "", "children": None,
                 "createTime": 1572318023000, "iframe": False},
                {"id": 54, "type": 2, "permission": "menu:del", "name": "菜单删除", "sort": 4, "path": "", "component": "",
                 "pid": 5, "cache": False, "hidden": False, "componentName": "", "icon": "", "children": None,
                 "createTime": 1572324960000, "iframe": False},
                {"id": 18, "type": 1, "permission": "storage:list", "name": "存储管理", "sort": 23, "path": "storage",
                 "component": "tools/storage/index", "pid": 36, "cache": False, "hidden": False,
                 "componentName": "Storage", "icon": "qiniu", "children": None, "createTime": 1546225935000,
                 "iframe": False},
                {"id": 28, "type": 1, "permission": "timing:list", "name": "定时任务", "sort": 21, "path": "timing",
                 "component": "system/timing/index", "pid": 36, "cache": False, "hidden": False,
                 "componentName": "Timing", "icon": "timing", "children": None, "createTime": 1546864480000,
                 "iframe": False}, {"id": 14, "type": 1, "permission": None, "name": "邮件", "sort": 24, "path": "email",
                                    "component": "tools/email/index", "pid": 36, "cache": False, "hidden": False,
                                    "componentName": "Email", "icon": "email", "children": None,
                                    "createTime": 1545876789000, "iframe": False},
                {"id": 6, "type": 0, "permission": None, "name": "系统监控", "sort": 20, "path": "monitor",
                 "component": None, "pid": 0, "cache": False, "hidden": False, "componentName": None, "icon": "monitor",
                 "children": None, "createTime": 1545117468000, "iframe": False},
                {"id": 9, "type": 1, "permission": None, "name": "SQL监控", "sort": 14, "path": "druid",
                 "component": "monitor/sql/index", "pid": 6, "cache": False, "hidden": False, "componentName": "Sql",
                 "icon": "sqlMonitor", "children": None, "createTime": 1545117574000, "iframe": False},
                {"id": 53, "type": 2, "permission": "menu:edit", "name": "菜单编辑", "sort": 3, "path": "", "component": "",
                 "pid": 5, "cache": False, "hidden": False, "componentName": "", "icon": "", "children": None,
                 "createTime": 1572324940000, "iframe": False},
                {"id": 36, "type": 0, "permission": None, "name": "系统工具", "sort": 60, "path": "sys-tools",
                 "component": "", "pid": 0, "cache": False, "hidden": False, "componentName": None, "icon": "sys-tools",
                 "children": None, "createTime": 1553828255000, "iframe": False},
                {"id": 44, "type": 2, "permission": "user:add", "name": "用户新增", "sort": 2, "path": "", "component": "",
                 "pid": 2, "cache": False, "hidden": False, "componentName": "", "icon": "", "children": None,
                 "createTime": 1572317986000, "iframe": False},
                {"id": 5, "type": 1, "permission": "menu:list", "name": "菜单管理", "sort": 5, "path": "menu",
                 "component": "system/menu/index", "pid": 1, "cache": False, "hidden": False, "componentName": "Menu",
                 "icon": "menu", "children": None, "createTime": 1545117448000, "iframe": False},
                {"id": 75, "type": 2, "permission": "timing:del", "name": "任务删除", "sort": 4, "path": "",
                 "component": "", "pid": 28, "cache": False, "hidden": False, "componentName": "", "icon": "",
                 "children": None, "createTime": 1572325674000, "iframe": False},
                {"id": 11, "type": 1, "permission": None, "name": "归档管理", "sort": 51, "path": "archiving",
                 "component": "archiving-sys/archiving/index", "pid": 10, "cache": False, "hidden": False,
                 "componentName": "Archiving", "icon": "icon", "children": None, "createTime": 1545197929000,
                 "iframe": False},
                {"id": 78, "type": 2, "permission": "storage:edit", "name": "文件编辑", "sort": 3, "path": "",
                 "component": "", "pid": 18, "cache": False, "hidden": False, "componentName": "", "icon": "",
                 "children": None, "createTime": 1572325762000, "iframe": False},
                {"id": 73, "type": 2, "permission": "timing:add", "name": "任务新增", "sort": 2, "path": "",
                 "component": "", "pid": 28, "cache": False, "hidden": False, "componentName": "", "icon": "",
                 "children": None, "createTime": 1572325648000, "iframe": False},
                {"id": 3, "type": 1, "permission": "roles:list", "name": "角色管理", "sort": 3, "path": "role",
                 "component": "system/role/index", "pid": 1, "cache": False, "hidden": False, "componentName": "Role",
                 "icon": "role", "children": None, "createTime": 1545117367000, "iframe": False},
                {"id": 38, "type": 1, "permission": None, "name": "接口文档", "sort": 26, "path": "swagger2",
                 "component": "tools/swagger/index", "pid": 36, "cache": False, "hidden": False,
                 "componentName": "Swagger", "icon": "swagger", "children": None, "createTime": 1553860673000,
                 "iframe": False},
                {"id": 50, "type": 2, "permission": "roles:del", "name": "角色删除", "sort": 4, "path": "", "component": "",
                 "pid": 3, "cache": False, "hidden": False, "componentName": "", "icon": "", "children": None,
                 "createTime": 1572324411000, "iframe": False},
                {"id": 2, "type": 1, "permission": "user:list", "name": "用户管理", "sort": 2, "path": "user",
                 "component": "system/user/index", "pid": 1, "cache": False, "hidden": False, "componentName": "User",
                 "icon": "peoples", "children": None, "createTime": 1545117284000, "iframe": False},
                {"id": 45, "type": 2, "permission": "user:edit", "name": "用户编辑", "sort": 3, "path": "", "component": "",
                 "pid": 2, "cache": False, "hidden": False, "componentName": "", "icon": "", "children": None,
                 "createTime": 1572318008000, "iframe": False},
                {"id": 74, "type": 2, "permission": "timing:edit", "name": "任务编辑", "sort": 3, "path": "",
                 "component": "", "pid": 28, "cache": False, "hidden": False, "componentName": "", "icon": "",
                 "children": None, "createTime": 1572325661000, "iframe": False},
                {"id": 7, "type": 1, "permission": None, "name": "操作日志", "sort": 11, "path": "logs",
                 "component": "monitor/log/index", "pid": 6, "cache": False, "hidden": False, "componentName": "Log",
                 "icon": "log", "children": None, "createTime": 1545117506000, "iframe": False},
                {"id": 1, "type": 0, "permission": None, "name": "系统管理", "sort": 40, "path": "system",
                 "component": None, "pid": 0, "cache": False, "hidden": False, "componentName": None, "icon": "system",
                 "children": None, "createTime": 1545117089000, "iframe": False},
                {"id": 15, "type": 1, "permission": None, "name": "归档策略管理", "sort": 52, "path": "arch-policy",
                 "component": "archiving-sys/arch-policy/index", "pid": 10, "cache": False, "hidden": False,
                 "componentName": "ArchPolicy", "icon": "fwb", "children": None, "createTime": 1545883105000,
                 "iframe": False},
                {"id": 10, "type": 0, "permission": None, "name": "归档系统", "sort": 1, "path": "archiving-sys",
                 "component": None, "pid": 0, "cache": False, "hidden": False, "componentName": None, "icon": "zujian",
                 "children": None, "createTime": 1545197896000, "iframe": False},
                {"id": 49, "type": 2, "permission": "roles:edit", "name": "角色修改", "sort": 3, "path": "",
                 "component": "", "pid": 3, "cache": False, "hidden": False, "componentName": "", "icon": "",
                 "children": None, "createTime": 1572324376000, "iframe": False},
                {"id": 52, "type": 2, "permission": "menu:add", "name": "菜单新增", "sort": 2, "path": "", "component": "",
                 "pid": 5, "cache": False, "hidden": False, "componentName": "", "icon": "", "children": None,
                 "createTime": 1572324907000, "iframe": False},
                {"id": 79, "type": 2, "permission": "storage:del", "name": "文件删除", "sort": 4, "path": "",
                 "component": "", "pid": 18, "cache": False, "hidden": False, "componentName": "", "icon": "",
                 "children": None, "createTime": 1572325774000, "iframe": False},
                {"id": 77, "type": 2, "permission": "storage:add", "name": "上传文件", "sort": 2, "path": "",
                 "component": "", "pid": 18, "cache": False, "hidden": False, "componentName": "", "icon": "",
                 "children": None, "createTime": 1572325749000, "iframe": False},
                {"id": 48, "type": 2, "permission": "roles:add", "name": "角色创建", "sort": 2, "path": "", "component": "",
                 "pid": 3, "cache": False, "hidden": False, "componentName": "", "icon": "", "children": None,
                 "createTime": 1572324334000, "iframe": False},
                {"id": 32, "type": 1, "permission": None, "name": "异常日志", "sort": 12, "path": "errorLog",
                 "component": "monitor/log/errorLog", "pid": 6, "cache": False, "hidden": False,
                 "componentName": "ErrorLog", "icon": "error", "children": None, "createTime": 1547358543000,
                 "iframe": False}], "depts": [], "createTime": 1542942277000},
            {"id": 2, "name": "普通用户", "dataScope": "自定义", "level": 2, "remark": "-", "permission": "common", "menus": [
                {"id": 1, "type": 0, "permission": None, "name": "系统管理", "sort": 40, "path": "system",
                 "component": None, "pid": 0, "cache": False, "hidden": False, "componentName": None, "icon": "system",
                 "children": None, "createTime": 1545117089000, "iframe": False},
                {"id": 15, "type": 1, "permission": None, "name": "归档策略管理", "sort": 52, "path": "arch-policy",
                 "component": "archiving-sys/arch-policy/index", "pid": 10, "cache": False, "hidden": False,
                 "componentName": "ArchPolicy", "icon": "fwb", "children": None, "createTime": 1545883105000,
                 "iframe": False}, {"id": 14, "type": 1, "permission": None, "name": "邮件", "sort": 24, "path": "email",
                                    "component": "tools/email/index", "pid": 36, "cache": False, "hidden": False,
                                    "componentName": "Email", "icon": "email", "children": None,
                                    "createTime": 1545876789000, "iframe": False},
                {"id": 28, "type": 1, "permission": "timing:list", "name": "定时任务", "sort": 21, "path": "timing",
                 "component": "system/timing/index", "pid": 36, "cache": False, "hidden": False,
                 "componentName": "Timing", "icon": "timing", "children": None, "createTime": 1546864480000,
                 "iframe": False},
                {"id": 3, "type": 1, "permission": "roles:list", "name": "角色管理", "sort": 3, "path": "role",
                 "component": "system/role/index", "pid": 1, "cache": False, "hidden": False, "componentName": "Role",
                 "icon": "role", "children": None, "createTime": 1545117367000, "iframe": False},
                {"id": 6, "type": 0, "permission": None, "name": "系统监控", "sort": 20, "path": "monitor",
                 "component": None, "pid": 0, "cache": False, "hidden": False, "componentName": None, "icon": "monitor",
                 "children": None, "createTime": 1545117468000, "iframe": False},
                {"id": 79, "type": 2, "permission": "storage:del", "name": "文件删除", "sort": 4, "path": "",
                 "component": "", "pid": 18, "cache": False, "hidden": False, "componentName": "", "icon": "",
                 "children": None, "createTime": 1572325774000, "iframe": False},
                {"id": 77, "type": 2, "permission": "storage:add", "name": "上传文件", "sort": 2, "path": "",
                 "component": "", "pid": 18, "cache": False, "hidden": False, "componentName": "", "icon": "",
                 "children": None, "createTime": 1572325749000, "iframe": False},
                {"id": 2, "type": 1, "permission": "user:list", "name": "用户管理", "sort": 2, "path": "user",
                 "component": "system/user/index", "pid": 1, "cache": False, "hidden": False, "componentName": "User",
                 "icon": "peoples", "children": None, "createTime": 1545117284000, "iframe": False},
                {"id": 5, "type": 1, "permission": "menu:list", "name": "菜单管理", "sort": 5, "path": "menu",
                 "component": "system/menu/index", "pid": 1, "cache": False, "hidden": False, "componentName": "Menu",
                 "icon": "menu", "children": None, "createTime": 1545117448000, "iframe": False},
                {"id": 38, "type": 1, "permission": None, "name": "接口文档", "sort": 26, "path": "swagger2",
                 "component": "tools/swagger/index", "pid": 36, "cache": False, "hidden": False,
                 "componentName": "Swagger", "icon": "swagger", "children": None, "createTime": 1553860673000,
                 "iframe": False},
                {"id": 78, "type": 2, "permission": "storage:edit", "name": "文件编辑", "sort": 3, "path": "",
                 "component": "", "pid": 18, "cache": False, "hidden": False, "componentName": "", "icon": "",
                 "children": None, "createTime": 1572325762000, "iframe": False},
                {"id": 36, "type": 0, "permission": None, "name": "系统工具", "sort": 60, "path": "sys-tools",
                 "component": "", "pid": 0, "cache": False, "hidden": False, "componentName": None, "icon": "sys-tools",
                 "children": None, "createTime": 1553828255000, "iframe": False},
                {"id": 10, "type": 0, "permission": None, "name": "归档系统", "sort": 1, "path": "archiving-sys",
                 "component": None, "pid": 0, "cache": False, "hidden": False, "componentName": None, "icon": "zujian",
                 "children": None, "createTime": 1545197896000, "iframe": False},
                {"id": 18, "type": 1, "permission": "storage:list", "name": "存储管理", "sort": 23, "path": "storage",
                 "component": "tools/storage/index", "pid": 36, "cache": False, "hidden": False,
                 "componentName": "Storage", "icon": "qiniu", "children": None, "createTime": 1546225935000,
                 "iframe": False},
                {"id": 11, "type": 1, "permission": None, "name": "归档管理", "sort": 51, "path": "archiving",
                 "component": "archiving-sys/archiving/index", "pid": 10, "cache": False, "hidden": False,
                 "componentName": "Archiving", "icon": "icon", "children": None, "createTime": 1545197929000,
                 "iframe": False},
                {"id": 9, "type": 1, "permission": None, "name": "SQL监控", "sort": 14, "path": "druid",
                 "component": "monitor/sql/index", "pid": 6, "cache": False, "hidden": False, "componentName": "Sql",
                 "icon": "sqlMonitor", "children": None, "createTime": 1545117574000, "iframe": False}],
             "depts": [{"id": 2, "name": "研发部", "enabled": True, "pid": 7, "createTime": 1553476532000, "label": "研发部"},
                       {"id": 5, "name": "运维部", "enabled": True, "pid": 7, "createTime": 1553476844000,
                        "label": "运维部"}], "createTime": 1542949746000}], "totalElements": 2}
        return Response(data=result, status=Constants.HTTP_200_CODE)

    def put(self, request):
        """

        :param request:
        :return:
        """
        pass

    def post(self, request):
        """

        :param request:
        :return:
        """
        pass
