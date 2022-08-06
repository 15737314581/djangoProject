from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import *


# Create your views here.

def index(request):
    # return HttpResponse("你好a～")
    return render(request, 'hello.html')


def hello_word(request):
    return HttpResponse("hello_world11")


def test_create(request):
    test = Test()
    test.name = 'huace_test'
    test.password = '123456'
    test.save()
    return HttpResponse('添加成功～')


def test_delete(request):
    delete_test = Test.objects.get(id=4)
    delete_test.delete()
    return HttpResponse('删除成功～')


def get_create_user_html(request):
    """
    进入创建用户的html页面
    :param request:
    :return:
    """
    return render(request, 'testapp/create_user.html')


def create_user(request):
    """
    创建用户
    :param request:
    :return:
    """
    username = request.POST['username']
    password = request.POST['password']
    # 方法一
    # User(username=username,password=password).save()
    # 方法二
    data = {"username": username, "password": password}
    obj = User.objects.all()
    obj.create(**data)
    return render(request, 'testapp/create_user.html')


def get_search_user_html(request):
    """
    进入搜索用户的html页面
    :param request:
    :return:
    """
    return render(request, 'testapp/search_user.html')


def search_user(request):
    """
    搜索用户
    :param request:
    :return:
    """
    search_username = request.GET['username']
    user_objs = User.objects.filter(username=search_username)
    user_data = []
    for user_obj in user_objs:
        data = {"id": user_obj.__dict__['id'],
                "username": user_obj.__dict__['username'],
                "password": user_obj.__dict__['password']}
        user_data.append(data)
    return render(request, 'testapp/search_user.html', context={"user_data": user_data})


def get_update_user_html(request):
    """
    进入修改用户的html页面
    :param request:
    :return:
    """
    user_objs = User.objects.all()
    user_data = []
    for user_obj in user_objs:
        data = {"id": user_obj.__dict__['id'],
                "username": user_obj.__dict__['username'],
                "password": user_obj.__dict__['password']}
        user_data.append(data)
    return render(request, 'testapp/update_user.html', context={"user_data": user_data})


def update_user(request):
    user_id = request.POST['id']
    username = request.POST['username']
    password = request.POST['password']
    user_obj = User.objects.get(id=user_id)
    user_obj.__dict__.update({"username": username, "password": password})
    user_obj.save()
    user_objs = User.objects.all()
    user_data = []
    for user_obj in user_objs:
        data = {"id": user_obj.__dict__['id'],
                "username": user_obj.__dict__['username'],
                "password": user_obj.__dict__['password']}
        user_data.append(data)
    return render(request, 'testapp/update_user.html', context={"user_data": user_data})
