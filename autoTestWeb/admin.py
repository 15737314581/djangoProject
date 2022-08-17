from django.contrib import admin

from .models import TestCase, CaseSet

# Register your models here.

admin.site.register(TestCase)
admin.site.register(CaseSet)