from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    role = models.ForeignKey("roles.Role", on_delete=models.SET_NULL, null=True, related_name='role_user')   # 不级联删除, 置空

    class Meta:
        db_table = 'user'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name