from django.db import models


# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=18)
    password = models.CharField(max_length=20)


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    #  DateTimeField 里面可以接参数 auto_now_add 是指使用第一次创建的时间自动存储；
    create_time = models.DateTimeField(auto_now_add=True)
    #  DateTimeField 里面可以接参数 auto_now 是指使用每次更新数据的时间自动存储；
    update_time = models.DateTimeField(auto_now=True)

