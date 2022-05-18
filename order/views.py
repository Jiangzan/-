from django.shortcuts import render, redirect

# Create your views here.
def Aorder_list(request):
    """ 管理员订单页面 """
    return render(request, 'Aorder_list.html')

def Aorder_add(request):
    """ 管理员订单添加页面 """
    return render(request, 'Aorder_add.html')

def Aorder_edit(request):
    """ 管理员订单编辑页面 """
    return render(request, 'Aorder_edit.html')

def Aorder_del(request):
    """ 管理员订单删除页面 """
    return redirect('/shop/admin/order/list/')

def shoppingcar(request):
    """ 用户购物车页面 """
    return render(request, 'shoppingcar.html')

def oder_processing(request):
    """ 用户订单提交/处理页面 """
    return render(request, "oder_processing.html")

def order_list(request):
    """ 用户订单页面 """
    return render(request, "order_list.html")

def order_success(request):
    """ 用户订单处理成功页面 """
    return render(request, "order_success.html")
