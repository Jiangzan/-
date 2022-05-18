from django.shortcuts import render,HttpResponse,redirect

from appUser.models import tb_user
"""用户登录界面"""
def user_login(request):
    return render(request, 'user_login.html')

"""用户中心界面"""
def user_home(request):
    return render(request, 'user_home.html')

"""用户主页"""
def user_info(request):
    return render(request, 'user_info.html')

"""消息中心"""
def user_answer(request):
    return render(request, 'user_answer.html')

"""修改个人信息"""
def user_detail(request):

    return render(request, 'user_detail.html')

"""留言板"""
def user_words(request):
    return render(request, 'user_words.html')

"""表头文件"""
def admin_layout(request):

    return render(request,'admin_layout.html')

"""管理员登录"""
def admin_login(request):
    return render(request, 'admin_login.html')

"""管理员信息"""
def admin_info(request):
    return render(request, 'admin_info.html')

"""管理员更改自身信息"""
def admin_form(request):
    return render(request, 'admin_form.html')

"""用户信息列表"""
def user_list(request):
    return render(request,'user_list.html')

"""添加用户"""
def user_add(request):
    return render(request,'user_add.html')

#删除用户
#def user_delete(request):

"""修改用户信息"""
def user_edit(request):
    return render(request,'user_edit.html')

"""主页面"""
def home_layout(request):
    return render(request,'home_layout.html')