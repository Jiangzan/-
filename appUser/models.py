from django.db import models

class tb_user(models.Model):
    """用户信息表"""
    name = models.CharField(verbose_name='姓名', max_length=25)
    password = models.CharField(verbose_name='密码',max_length=50)
    dongjie = models.IntegerField()#用户是否冻结
    email = models.CharField(verbose_name='邮箱',max_length=25)
    tel = models.CharField(verbose_name='联系电话',max_length=25)
    dizhi = models.CharField(verbose_name='地址',max_length=100)
    youbian = models.CharField(verbose_name='邮编',max_length=25)
    truename = models.CharField(verbose_name='真实姓名',max_length=25)
    regtime = models.CharField(max_length=25)#注册时间
    lastlogintime = models.CharField(max_length=25)#最近一次登录时间
    logincishu = models.IntegerField(4)#登录次数