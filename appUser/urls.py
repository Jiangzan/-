"""MyUser URL Configuration

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
from appUser import views
app_name='appUser'
urlpatterns = [
    path('user/login/', views.user_login,name='user_login'),  #用户登录
    path('user/home/', views.user_home),
    path('user/info/', views.user_info),
    path('user/answer/', views.user_answer),
    path('user/detail/', views.user_detail),
    path('user/words/', views.user_words),
    path('admin/layout/', views.admin_layout),
    path('admin/login/', views.admin_login),
    path('admin/info/', views.admin_info,name='manager_list'), #管理员列表
    path('admin/form/', views.admin_form),
    path('user/list/', views.user_list,name='user_list'), # 用户列表
    path('user/add/', views.user_add),
    # path('user/delete/',views.user_delete),
    path('user/edit/', views.user_edit),
]
