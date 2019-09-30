# -*- coding: UTF-8 -*-
##########################################################################
# File Name: users/urls.py
# Author: Wang Yuan
# mail: 853283581@qq.com
# Created Time: 2019年09月23日 星期一 11时26分43秒
#########################################################################
#!/usr/bin/env python
# coding=utf-8

"""未应用程序users定义URL模式"""
from django.conf.urls import url
from django.contrib.auth.views import LoginView
#from django.contrib.auth import login

from . import views

app_name = 'login'
app_name = 'logout'
app_name = 'register'
urlpatterns = [
    #登陆页面
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
    #注销
    url(r'^logout/$', views.logout_view, name='logout'),
    #注册页面
    url(r'^register/$', views.register, name='register'),
]
