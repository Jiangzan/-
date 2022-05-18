from db.base_model import BaseModel
from django.db import models
# from tinymce.models import HTMLField
from goods.enums import *

# class GoodsManager(models.Manager):
#     '''商品模型管理器类'''
#     # sort='new' 按照创建时间进行排序
#     # sort='hot' 按照商品销量进行排序
#     # sort='price' 按照商品的价格进行排序
#     # sort= 按照默认顺序排序
#     def get_goods_by_type(self, type_id, limit=None, sort='default'):
#         '''根据商品类型id查询商品信息'''
#         if sort == 'new':
#             order_by = ('-create_time',)
#         elif sort == 'hot':
#             order_by = ('-sales', )
#         elif sort == 'price':
#             order_by = ('price', )
#         else:
#             order_by = ('-pk', ) # 按照primary key降序排列。
#
#         # 查询数据
#         goods_li = self.filter(type_id=type_id).order_by(*order_by)
#
#         # 查询结果集的限制
#         if limit:
#             goods_li = goods_li[:limit]
#         return goods_li
#
#     def get_goods_by_id(self, goods_id):
#         '''根据商品的id获取商品信息'''
#         try:
#             books = self.get(id=goods_id)
#         except self.model.DoesNotExist:
#             # 不存在商品信息
#             books = None
#         return books



class Goods(BaseModel):
    '''商品模型类'''
    goods_type_choices = ((k, v) for k,v in GOODS_TYPE.items())
    status_choices = ((k, v) for k,v in STATUS_CHOICE.items())
    size_choices =((k, v) for k,v in SIZE_CHOICE.items())
    sale_choices = ((k, v) for k, v in SALE_CHOICE .items())

    mingcheng = models.CharField(max_length=25, verbose_name='商品名称')
    jianjie = models.CharField(max_length=128, verbose_name='商品简介',null=True, blank=True)
    type_id = models.SmallIntegerField(default=COMPUTER, choices=goods_type_choices, verbose_name='商品种类')
    xinghao = models.SmallIntegerField(choices=size_choices, verbose_name="商品型号",null=True, blank=True)
    image = models.ImageField(upload_to='goods', verbose_name='商品图片',null=True, blank=True)
    status = models.SmallIntegerField(default=OFFLINE, choices=status_choices, verbose_name="商品状态")
    sales = models.IntegerField(default=0, verbose_name='商品销量')
    stock = models.IntegerField(default=1, verbose_name='商品库存')
    huiyuanjia = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="会员价")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="市场价")
    tejia = models.IntegerField(default=NOSALE,choices=sale_choices,verbose_name="是否为特价商品")
    pinpai = models.CharField(max_length=25,verbose_name="商品品牌")
    # detail = HTMLField(verbose_name='商品详情')

    #objects = GoodsManager()

    # admin显示商品的名字
    def __str__(self):
        return self.mingcheng

    class Meta:
        db_table = 's_goods' #自定义表名
        verbose_name = '商品'
        verbose_name_plural = '商品'
