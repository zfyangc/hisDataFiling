# coding:utf-8
from rest_framework import serializers

from menu.serializers import MenuSerializer
from .models import Role


class RoleSerializer(serializers.ModelSerializer):
    menu = MenuSerializer(many=True)
    class Meta:
        model = Role
        fields = "__all__"
