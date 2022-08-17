from django.contrib import admin

from .models import User


# Register your models here.

# admin.site.register(User,UserAdmin) 等同于装饰器

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # 设置列表显示字段
    list_display = ['username', 'password', 'update_time']
    # 分页
    list_max_show_all = 10 # 页面最大显示数据
    list_per_page = 10 # 页面显示数据
    # 排序 字段名前加"+"或者不加符合表示正序，"-"表示倒序
    ordering = ('-id',)


