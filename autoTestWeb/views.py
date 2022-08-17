from django.shortcuts import render

from .models import *


# Create your views here.

def get_create_case_html(request):
    """
    进入创建case的html页面
    :param request:
    :return:
    """
    case_objs = TestCase.objects.all()
    case_data = []
    for case_obj in case_objs:
        data = {'case_name': case_obj.__dict__['case_name'],
                'browser': case_obj.__dict__['browser'],
                'url': case_obj.__dict__['url']}
        case_data.append(data)
    return render(request, 'autoTestWeb/create_case.html', context={'case_data': case_data})


def create_case(request):
    """
    创建用例
    :param request:
    :return:
    """
    case_name = request.POST['case_name']
    browser = request.POST['browser']
    url = request.POST['url']
    TestCase(case_name=case_name, browser=browser, url=url).save()
    case_objs = TestCase.objects.all()
    case_data = []
    for case_obj in case_objs:
        data = {'case_name': case_obj.__dict__['case_name'],
                'browser': case_obj.__dict__['browser'],
                'url': case_obj.__dict__['url']}
        case_data.append(data)

    return render(request, 'autoTestWeb/create_case.html', context={'case_data': case_data})
