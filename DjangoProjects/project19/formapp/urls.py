from django.urls import path

from formapp import views

urlpatterns=[
	path('formPage/', views.student_form),
]