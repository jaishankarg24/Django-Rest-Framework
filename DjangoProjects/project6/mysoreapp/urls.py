from mysoreapp import views as mysore
from django.urls import path
urlpatterns=[
    path('mysore/ramakrishnanagar', mysore.ramakrishnanagar_cases),
    path('mysore/basavanagudi', mysore.basavanagudi_cases),
    path('mysore/vijaynagar', mysore.vijaynagar_cases),
]