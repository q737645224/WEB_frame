from django.db import models

# Create your models here.
#在index应用中的models.py中
# 创建一个实体类 - Publisher
# 用于表示出版社信息，属性如下
# 1.name：出版社名称(varchar)
# 2.address：出版社所在地址(varchar)
 # 3.city：出版社所在城市(varchar)
# 4.country：出版社所在国家(varchar)
# 5.website：出版社的网址(varchar)
#db.Model
class Publisher(models.Model):
    name = models.CharField(max_length=30)  #db.Cluom()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    website = models.URLField()  #默认长度为２００


# 1.Author - 作者
#     1.name - 姓名
#     2.age - 年龄
#     3.email - 邮箱(允许为空)
# 2.Book - 图书
#     1.title - 书名
#     2.publicate_date - 出版时间

class Author(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    emil = models.EmailField(null=True)

class Book(models.Model):
    title = models.CharField(max_length=30)
    publicate_date = models.DateField()

