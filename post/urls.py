# -*- coding: utf-8 -*-
# @Time : 2020/7/12 15:39
# @Author : Allenware
# @File : urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_index, name='post_index'),
    path('<int:post_id>/', views.post_detail, name='post_detail')
]
