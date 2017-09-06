# _*_ coding: utf-8 _*_
__author__ = 'xiehao'
__date__ = '2017/9/6 下午8:24'


import xadmin
from .models import BlogsWord


class BlogsWordAdmin(object):
    pass

xadmin.site.register(BlogsWord, BlogsWordAdmin)