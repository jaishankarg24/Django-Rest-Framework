from bengaluruapp import views as bengaluru
from django.urls import path

urlpatterns=[
	path('bengaluru/vijaynagar', bengaluru.vijaynagar_cases),
    path('bengaluru/btm', bengaluru.btm_cases),
    path('bengaluru/hebbal', bengaluru.hebbal_cases),
]