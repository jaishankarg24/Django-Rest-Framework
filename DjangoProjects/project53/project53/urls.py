"""project53 URL Configuration

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
from django.contrib import admin
from django.urls import path, re_path
from crudapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.CompanyHome.as_view()),
    path('display/', views.CompanyListview.as_view(), name='companylist'),
    re_path(r'^(?P<pk>\d+)/$', views.CompanyDetailView.as_view(), name='detail'),
    path('create/', views.CompanyCreateView.as_view()),
    re_path(r'^update/(?P<pk>\d+)/$', views.CompanyUpdateView.as_view()),
    re_path(r'^delete/(?P<pk>\d+)/$', views.CompanyDeleteView.as_view()),

]
