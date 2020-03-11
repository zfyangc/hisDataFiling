# coding:utf-8
from rest_framework import serializers

from .models import Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class MenuTreeSerializer(serializers.ModelSerializer):
    label = serializers.CharField(source='name')

    class Meta:
        model = Menu
        fields = (
            'id', 'label'
        )


class MenuBuildSerializer(serializers.ModelSerializer):
    meta = serializers.SerializerMethodField(method_name="get_meta")
    alwaysShow = serializers.SerializerMethodField(method_name="get_alwaysShow")
    redirect = serializers.SerializerMethodField(method_name="get_redirect")
    path = serializers.SerializerMethodField(method_name="get_path", source="path")
    name = serializers.SerializerMethodField(method_name="get_name", source="name")
    class Meta:
        model = Menu
        fields = (
            "id",
            "name",
            "path",
            "hidden",
            "redirect",
            "component",
            "alwaysShow",
            "meta",
            "redirect",
            "type"
        )

    def get_meta(self, obj):
        return {"title": obj.name, "icon": obj.icon, "noCache": obj.cache}

    def get_alwaysShow(self, obj):
        return True

    def get_redirect(self, obj):
        return "noredirect"

    def get_path(self, obj):
        if obj.type == 0:
            if obj.path != '':
                return '/'+obj.path
        else:
            return obj.path

    def get_name(self, obj):
        if obj.component_name !='':
            return obj.component_name
        else:
            return obj.name
