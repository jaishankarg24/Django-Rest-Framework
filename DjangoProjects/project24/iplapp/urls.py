from django.urls import path

from iplapp import views

urlpatterns=[
	path('display/', views.display_page),
	path('addplayer/', views.addplayer),
	path('playerlist/', views.playerlist),
]