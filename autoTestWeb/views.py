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


def get_create_set_html(request):
    """
    进入创建case步骤的html页面
    :param request:
    :return:
    """
    case_set_objs = CaseSet.objects.all().order_by('id')
    case_set_data = []
    for case_set_obj in case_set_objs:
        testCase_id = case_set_obj.__dict__['testCase_id']
        testCase_obj = TestCase.objects.get(id=testCase_id)
        data = {'id': case_set_obj.__dict__['id'],
                'testCase': testCase_obj.case_name,
                'sort': case_set_obj.__dict__['sort'],
                'search_type': case_set_obj.__dict__['search_type'],
                'search_value': case_set_obj.__dict__['search_value'],
                'action': case_set_obj.__dict__['action'],
                'send_keys_value': case_set_obj.__dict__['send_keys_value']}
        case_set_data.append(data)
    testCase_objs = TestCase.objects.all()
    case_name_data = []
    for testCase_obj in testCase_objs:
        case_name_data.append(testCase_obj.case_name)
    return render(request, 'autoTestWeb/create_set.html',
                  context={'case_set_data': case_set_data, 'case_name_data': case_name_data})


def create_set(request):
    """
    创建测试步骤
    :param request:
    :return:
    """
    sort = request.POST['sort']
    search_type = request.POST['search_type']
    search_value = request.POST['search_value']
    action = request.POST['action']
    if action == 'send_keys':
        send_keys_value = request.POST['send_keys_value']
    else:
        send_keys_value = None
    testCase = request.POST.get('testCase')
    testCase_id = TestCase.objects.get(case_name=testCase).id
    CaseSet(sort=sort,
            search_type=search_type,
            search_value=search_value,
            action=action,
            send_keys_value=send_keys_value,
            testCase_id=testCase_id).save()

    case_set_objs = CaseSet.objects.all().order_by('id')
    case_set_data = []
    for case_set_obj in case_set_objs:
        testCase_id = case_set_obj.__dict__['testCase_id']
        testCase_obj = TestCase.objects.get(id=testCase_id)
        data = {'id': case_set_obj.__dict__['id'],
                'testCase': testCase_obj.case_name,
                'sort': case_set_obj.__dict__['sort'],
                'search_type': case_set_obj.__dict__['search_type'],
                'search_value': case_set_obj.__dict__['search_value'],
                'action': case_set_obj.__dict__['action'],
                'send_keys_value': case_set_obj.__dict__['send_keys_value']}
        case_set_data.append(data)
    testCase_objs = TestCase.objects.all()
    case_name_data = []
    for testCase_obj in testCase_objs:
        case_name_data.append(testCase_obj.case_name)
    return render(request, 'autoTestWeb/create_set.html',
                  context={'case_set_data': case_set_data, 'case_name_data': case_name_data})


def run(request):
    """
    运行用例
    :param request:
    :return:
    """
    runcase_id = int(request.POST['case_id'])
    case = TestCase.objects.get(id=runcase_id)
    browser = case.browser
    url = case.url
    case_set = CaseSet.objects.filter(testCase_id=runcase_id).order_by('sort')

    from selenium import webdriver
    driver = None
    if browser == 'chrome':
        driver = webdriver.Chrome()
    driver.get(url)
    for set in case_set:
        print(set.sort)
        element = driver.find_element(set.search_type, set.search_value)
        if set.action == 'click':
            element.click()
        if set.action == 'send_keys':
            element.send_keys(set.send_keys_value)
        if set.action == 'clear':
            element.clear()
    case_objs = TestCase.objects.all()
    case_data = []
    for case_obj in case_objs:
        data = {'case_name': case_obj.__dict__['case_name'],
                'browser': case_obj.__dict__['browser'],
                'url': case_obj.__dict__['url']}
        case_data.append(data)

    return render(request, 'autoTestWeb/create_case.html', context={'case_data': case_data})
