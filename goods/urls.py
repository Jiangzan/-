from django.urls import path
from goods import views # 从自己的 app 目录引入 views
app_name='goods'
urlpatterns = [
    path("goods/list/",views.goods_list, name='good_list'),
    path("goods/add/",views.goods_add),
    path("goods/<int:nid>/edit/",views.goods_edit),
    path("goods/<int:nid>/delete/",views.goods_delete),
    path('index/', views.index,name='index'),
    path('search/', views.search,name='search'),
]