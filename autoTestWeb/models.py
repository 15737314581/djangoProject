from django.db import models

# Create your models here.
# from selenium.webdriver.common.by import By

BROWSER_CHOICES = (
    ('chrome', 'chrome'),
    ('firefox', 'firefox'),
    ('IE', 'IE'),
)

SEARCH_TYPE_CHOICES = (
    ("ID", "id"),
    ("XPATH", "xpath"),
    ("LINK_TEXT", "link text"),
    ("PARTIAL_LINK_TEXT", "partial link text"),
    ("NAME", "name"),
    ("TAG_NAME", "tag name"),
    ("CLASS_NAME", "class name"),
    ("CSS_SELECTOR", "css selector"),
)

ACTION_CHOICES = (
    ("点击", "click"),
    ("输入文字", "send_keys"),
    ("清楚文本", "clear"),
)


class TestCase(models.Model):
    case_name = models.CharField(verbose_name='用例名称', max_length=200)
    browser = models.CharField(verbose_name='浏览器', max_length=200, choices=BROWSER_CHOICES)
    url = models.CharField(verbose_name='被测网址', max_length=200)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)

    class Meta:
        verbose_name_plural = '测试用例'

    def __str__(self):
        return self.case_name


class CaseSet(models.Model):
    sort = models.IntegerField(verbose_name='测试步骤', null=False, default=1)
    search_type = models.CharField(verbose_name='定位方式', max_length=200, choices=SEARCH_TYPE_CHOICES)
    search_value = models.CharField(verbose_name='定位值', max_length=200)
    action = models.CharField(verbose_name='操作方式', max_length=200, choices=ACTION_CHOICES)
    send_keys_value = models.CharField(verbose_name='输入内容', max_length=200, blank=True)
    testCase = models.ForeignKey(to=TestCase, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'web测试用例操作步骤'
        ordering = ('sort',)

    def __str__(self):
        return '操作步骤'
