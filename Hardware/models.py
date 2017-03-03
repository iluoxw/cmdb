# coding: utf-8
from django.db import models


class Hardware(models.Model):
    hdName = models.CharField(max_length=32,verbose_name="Hardware Name")
    hdCode = models.CharField(max_length=32,verbose_name="Hardware Code")
    hdDesc = models.TextField(blank=True, null=True,verbose_name="Hardware Description")  # 将字段设置为默认为空
    hdType = models.CharField(max_length=16,verbose_name="Hardware Type")
