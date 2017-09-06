# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.


class BlogsWord(models.Model):
    title = models.CharField(max_length=150, verbose_name=u'标题')
    body = models.TextField(verbose_name=u'内容')
    timestamp = models.DateTimeField(verbose_name=u'编辑时间')

    class Meta:
        verbose_name = u'博客文章'
        verbose_name_plural = verbose_name

