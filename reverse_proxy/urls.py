"""reverse_proxy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from django.conf.urls import url, include
from .views import generic_caching_view, manual_caching_view, test_caching_view
from django.urls import re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include('rp_app.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    re_path('.*', manual_caching_view),
]
