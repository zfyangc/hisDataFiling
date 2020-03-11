# coding:utf-8
from rest_framework import serializers

from roles.serializers import RoleSerializer
from .models import User


class UserInfoSerializer(serializers.ModelSerializer):
    staff_map = {
        1: '具有管理后台权限',
        0: '不具备后台管理权限'
    }
    active_map = {
        1: '激活',
        0: '禁止'
    }

    is_staff_value = serializers.SerializerMethodField(method_name='get_is_staff')
    is_active_value = serializers.SerializerMethodField(method_name='get_is_active')
    role = RoleSerializer()

    class Meta:
        model = User
        fields = (
            'id', 'is_superuser', 'username', 'email', 'is_staff', 'is_active', 'date_joined',
            'is_staff_value', 'is_active_value', 'role'
        )

    def get_is_staff(self, obj):
        return self.staff_map.get(obj.is_staff)

    def get_is_active(self, obj):
        return self.active_map.get(obj.is_active)
