from django.urls import path

from displaytimeapp import views

urlpatterns=[
	path('message/', views.display_time),
]