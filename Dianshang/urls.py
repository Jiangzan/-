"""Dianshang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from app01 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('tinymce/', include('tinymce.urls')),
    path('', include('goods.urls', namespace='goods')), # 商品模块
    path('', include('appUser.urls', namespace='appUser')),  # 商品模块
    path('', include('order.urls', namespace='order')),  # 订单模块
    path('', include('app01.urls', namespace='detail')),  # 商品详情
]

