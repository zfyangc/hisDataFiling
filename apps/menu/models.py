from django.db import models

# Create your models here.

class Menu(models.Model):
    id = models.AutoField(primary_key=True, blank=False, verbose_name='主键')
    i_frame = models.BooleanField(default=False, verbose_name='是否为外链')
    name = models.CharField(max_length=255, blank=False, verbose_name='菜单名称')
    component = models.CharField(max_length=255, blank=True, verbose_name="组件")
    pid = models.IntegerField(blank=True, verbose_name="上级菜单ID")
    sort = models.IntegerField(blank=True, verbose_name="排序")
    icon = models.CharField(max_length=255, blank=True, verbose_name="图标")
    path = models.CharField(max_length=255, blank=True, verbose_name="链接地址")
    cache = models.BooleanField(default=False, verbose_name="是否缓存")
    hidden = models.BooleanField(default=False, verbose_name="是否隐藏")
    component_name = models.CharField(max_length=255, blank=True, verbose_name="组件名称", default='-')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    permission = models.CharField(max_length=255, blank=True, verbose_name="权限")
    type = models.IntegerField(blank=True, verbose_name="菜单类型")

    class Meta:
        db_table = 'menu'
        verbose_name = '菜单信息'
        verbose_name_plural = verbose_name