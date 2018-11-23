from django.db import models

# Create your models here.
#编写GoodsType实体类
class GoodsType(models.Model):
    title = models.CharField(max_length=50,verbose_name='类型名称')
    desc = models.TextField(verbose_name='类型描述')
    picture = models.ImageField(upload_to='static/upload/goodstype',null=True,verbose_name='类型图片')
    def to_dict(self):
        dic = {
            "title":self.title,
            "desc":self.desc,
            "picture":self.picture.__str__(),
        }
        return dic
    class Meta:
        db_table='goods_type'
        verbose_name = '商品类型'
        verbose_name_plural = verbose_name

class Goods(models.Model):
    title = models.CharField(max_length=50,verbose_name='商品名称')
    price = models.DecimalField(max_digits=7,decimal_places=2,verbose_name='商品价格')
    spec = models.CharField(max_length=20,verbose_name='商品规格')
    picture = models.ImageField(upload_to='static/upload/goods',verbose_name='商品图片')
    #与商品类型的关系
    goodsType = models.ForeignKey(GoodsType,verbose_name='商品类型')
    isActive = models.BooleanField(default=True,verbose_name='是否上架')

    def to_dict(self):
        dic = {
            "title":self.title,
            "price":self.price,
            "spec":self.spec,
            "picture":self.picture.__str__(),
            "goodsType":self.goodsType,
            "isActive":self.isActive,
        }
        return dic

    def __str__(self):
        return self.title
    class Meta:
        db_table='goods'
        verbose_name = '商品'
        verbose_name_plural = verbose_name

class Users(models.Model):
    uphone = models.CharField(max_length=11,verbose_name='手机号')
    upwd = models.CharField(verbose_name='密码',max_length=20)
    uemail = models.EmailField(verbose_name='用户邮箱',max_length=30)
    uname = models.CharField(verbose_name='用户名',max_length=30)
    isActive = models.BooleanField(default=True,verbose_name='是否激活')
    def __str__(self):
        return self.uname
    class Meta:
        db_table='users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
