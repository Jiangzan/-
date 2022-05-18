from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from goods import models
from goods.form import GoodModelForm

def index(request):
    # 寻找index.html顺序（setting dir app下templates）
    return render(request, 'index.html')

def search(request):
    # 寻找index.html顺序（setting dir app下templates）
    return render(request, 'search_list.html')

def goods_list(request):
    # 寻找index.html顺序（setting dir app下templates）
    queryset = models.Goods.objects.all().order_by("-id")
    return render(request, 'admin_goods.html',{"queryset":queryset})


def goods_add(request):
    """添加用户（ModelForm版本）"""

    if request.method=='GET':
        form=GoodModelForm()
        return render(request,'admin_goods_add.html',{'form':form})

    # 用户POST提交数据，数据校验。
    form=GoodModelForm(data=request.POST,files=request.FILES)
    if form.is_valid():
        #默认保存用户在表单上输入的所有信息，如果想要用户在输入以外再增加一些值
        # form.instance.字段名 = 值
        form.save()
        return HttpResponse("成功")
    return render(request,'admin_goods_add.html',{'form':form})

def goods_edit(request,nid):
    row_object = models.Goods.objects.filter(id=nid).first()
    if request.method=='GET':
        form=GoodModelForm(instance=row_object)
        return render(request,'admin_goods_edit.html',{'form':form})
    form = GoodModelForm(data=request.POST)
    if form.is_valid():
        # 默认保存用户在表单上输入的所有信息，如果想要用户在输入以外再增加一些值
        # form.instance.字段名 = 值
        form.save()
        return redirect('/goods/list/')
    return render(request, 'admin_goods_edit.html', {'form': form})

def goods_delete(request,nid):
    row_object = models.Goods.objects.filter(id=nid).first().delete()
    return redirect('/goods/list/')