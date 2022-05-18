from django.urls import path

from order import views
app_name = 'order'
urlpatterns = [
    path('shop/admin/order/list/', views.Aorder_list,name='admin_order_list'),      # 管理员订单页面
    path('shop/admin/order/add/', views.Aorder_add),        # 管理员订单添加页面
    path('shop/admin/order/edit/', views.Aorder_edit),      # 管理员订单编辑页面
    path('shop/admin/order/del/', views.Aorder_del),        # 管理员订单删除页面
    path('shop/user/shoppingcar/', views.shoppingcar,name='shoppingcar'),      # 用户购物车页面
    path('shop/user/order/processing/', views.oder_processing,name='商城'), # 用户订单处理页面(购物车选择物品后的处理页面)
    path('shop/user/order/success/', views.order_success,name='order_dispose'),  # 订单处理成功页面
    path('shop/user/order/list/', views.order_list,name='order_list'),        # 用户-我的订单页面
]