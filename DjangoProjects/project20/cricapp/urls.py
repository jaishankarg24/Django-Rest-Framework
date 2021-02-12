from django.urls import path

from cricapp import views

urlpatterns = [
	path('formPage/', views.cricketer_form),

]