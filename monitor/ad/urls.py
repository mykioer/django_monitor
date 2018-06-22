#!/usr/bin/env python
#coding=utf-8
"""day11 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from .views import *

from django.urls import path

import sys

#dir_path = sys.path[1]
sys.path.append('G:\python\eclipse\day11\day11')



'''
urlpatterns = [
    path(r'^admin/', admin.site.urls),

    path(r'^index/$', index),
    path(r'^login/$', login),
    path(r'^list/(\d*)/$', list),
    path(r'^list2/(?P<name>\d*)/$', list2),
    path(r'^list2/(?P<alex>\d*)/$', list2,{'id':222}),
    path(r'^web/', include('web.url')),
    path(r'^ad/', include('ad.url'))
    
]
'''
urlpatterns = [
    #path(r'admin/', admin.site.urls),
    #path(r'^index/$', index),
    path(r'login/', login),
    #path(r'^add/(?P<name>\d*)/$', Add),
    #path(r'^delete/(?P<id>\d*)/$', Delete),
    path(r'assetupdate/', AssetUpdate),
    path(r'userupdate/', UserUpdate),
    #path(r'^updatetomany/(?P<id>\d*)/(?P<hostname>\w*)/$', UpdatetoMany),
    #path(r'^get/(?P<hostname>\w*)/$', Get),
    path(r'assetlist/', AssetList),
    path(r'register/', Register),
    path(r'userlist/', UserList),
    path(r'auth/', auth),
    path(r'monitor/warning/', server_monitor_warning),
    path(r'monitor/hostgroup/', server_monitor_hostgroup),
    path(r'monitor1/', server_monitor1),
    path(r'monitor/templates/', server_monitor_templates),
    path(r'monitor/triggers/', server_monitor_triggers),
    path(r'monitor/message/<int:id>/', server_monitor_message),
    path(r'monitor/<name>/', server_monitor),
]
