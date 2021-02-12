from django.urls import path

from timeapp import views

urlpatterns=[
	path('message/', views.display_time),
]