"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app01 import views
app_name='detail'
urlpatterns = [
    path('admin/judge/list/', views.admin_judge_list,name='judge_list'),
    path('admin/words/list/', views.admin_words_list,name='user_words'),
    path('admin/reply/words/', views.admin_reply_words),
    path('admin/notice/list/', views.admin_notice_list,name='notice_add'),
    path('admin/notice/add/', views.admin_notice_add),
    path('admin/notice/edit/', views.admin_notice_edit),
    path('detail/', views.detail),
    path('goods/judge/', views.goods_judge),
]
