from django.urls import path

from ndtvapp import views

urlpatterns = [
	path('HomePage/', views.home_page),
	path('MoviesPage/', views.display_movies_information),
	path('PoliticsPage/', views.display_politics_information),
	path('SportsPage/', views.display_sports_information),
]