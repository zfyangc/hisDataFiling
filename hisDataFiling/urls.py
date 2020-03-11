"""hisDataFiling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path(r'auth/', include('sys_auth.urls')),
    path(r'api/menus/', include('menu.urls')),
    path(r'api/visits/', include('visits.urls')),
    path(r'api/logs/', include('log_manage.urls')),
    path(r'api/users/', include('users.urls')),
    path(r'api/roles/', include('roles.urls')),


]
