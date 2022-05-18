from goods import models
from goods.bootstrap import BootstrapModleFrom

# 创建添加表单的类，并继承bootstrap样式
class GoodModelForm(BootstrapModleFrom):
    bootstrap_exclude_fields = ['image']

    class Meta:
        model = models.Goods
        fields= "__all__"
        exclude=['create_time','update_time']

