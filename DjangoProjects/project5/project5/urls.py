"""project5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from bengaluruapp import views as bengaluru
from mysoreapp import views as mysore
from shimogaapp import views as shimoga

urlpatterns = [
    path('admin/', admin.site.urls),

    path('bengaluru/vijaynagar', bengaluru.vijaynagar_cases),
    path('bengaluru/btm', bengaluru.btm_cases),
    path('bengaluru/hebbal', bengaluru.hebbal_cases),

    path('mysore/ramakrishnanagar', mysore.ramakrishnanagar_cases),
    path('mysore/basavanagudi', mysore.basavanagudi_cases),
    path('mysore/vijaynagar', mysore.vijaynagar_cases),

    path('shimoga/ravindranagar', shimoga.ravindranagar_cases),
    path('shimoga/gopala', shimoga.gopala_cases),
    path('shimoga/bapujinagar', shimoga.bapujinagar_cases),
]
