"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from autoTestWeb.views import *
from testapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('index/', index),
    path('hello/', hello_word),
    path('create1/', test_create),
    path('delete/', test_delete),
    path('create/', get_create_user_html),
    path('create/user/', create_user),
    path('search/', get_search_user_html),
    path('search/user/', search_user),
    path('update/', get_update_user_html),
    path('update/user/', update_user),
    path('at_create/', get_create_case_html),
    path('at_create/case', create_case)
]
