from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Test


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
