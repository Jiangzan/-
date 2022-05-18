from django.shortcuts import render


def admin_layout(request):
    return render(request, 'admin_layout.html')


def admin_judge_list(request):
    return render(request, 'admin_judge_list.html')


def admin_words_list(request):
    return render(request, 'admin_words_list.html')


def admin_reply_words(request):
    return render(request, 'admin_reply_words.html')


def admin_notice_list(request):
    return render(request, 'admin_notice_list.html')


def admin_notice_add(request):
    return render(request, 'admin_notice_add.html')


def admin_notice_edit(request):
    return render(request, 'admin_notice_edit.html')


def detail(request):
    return render(request, 'detail.html')


def goods_judge(request):
    return render(request, 'goods_judge.html')


# Create your views here.
