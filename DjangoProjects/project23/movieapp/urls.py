from django.urls import path

from movieapp import views

urlpatterns=[
	path('display/', views.display_page),
	path('addmovie/', views.addmovie),
	path('showmovie/', views.showmovie),
]