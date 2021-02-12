from django.urls import path

from studentapp import views

urlpatterns=[
	path('homepage/', views.home_page),
	path('feedback/', views.feedback),
	path('thankyou/', views.thankyou),
]