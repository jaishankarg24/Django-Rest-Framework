from django.urls import path

from modelformapp import views

urlpatterns = [

	path('display/', views.display_page),
]