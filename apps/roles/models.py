from django.db import models

# Create your models here.

class Role(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    name = models.CharField(max_length=64, blank=False)
    level = models.IntegerField(blank=False)
    create_time = models.DateTimeField(auto_now_add=True)
    menu = models.ManyToManyField("menu.Menu", related_name="menu")

    class Meta:
        db_table = 'role'
        verbose_name = '角色'
        verbose_name_plural = verbose_name

