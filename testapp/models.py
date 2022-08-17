from django.db import models


# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=18)
    password = models.CharField(max_length=20)


class User(models.Model):
    username = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=20, verbose_name='密码')
    #  DateTimeField 里面可以接参数 auto_now_add 是指使用第一次创建的时间自动存储；
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    #  DateTimeField 里面可以接参数 auto_now 是指使用每次更新数据的时间自动存储；
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        """
        通过魔方方法去自定义返回对象
        :return:
        """
        return self.username

    class Meta:
        # 设置数据模型的别名，尽量使用复数别名
        verbose_name_plural = "签到用户"
