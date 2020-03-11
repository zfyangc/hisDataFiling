from django.db import models

# Create your models here.

class StorageSource(models.Model):
    id = models.AutoField(primary_key=True, blank=False, verbose_name='主键')
    name = models.CharField(max_length=64, blank=False, verbose_name="数据库连接名称")
    ip = models.CharField(max_length=64, blank=False, verbose_name="数据库地址")
    port = models.IntegerField(blank=False, verbose_name="数据库端口")
    db_type = models.CharField(max_length=64, blank=False, verbose_name="数据库类型")
    username = models.CharField(max_length=64, blank=False, verbose_name="用户名")
    password = models.CharField(max_length=64, blank=False, verbose_name="密码")
    type = models.IntegerField(blank=False, verbose_name="存储类型")

    class Meta:
        db_table = 'storage_source'
        verbose_name = '存储源'
        verbose_name_plural = verbose_name


