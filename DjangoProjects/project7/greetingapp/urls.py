from django.urls import path
from greetingapp import views

urlpatterns = [
	path('message/', views.welcome),
]