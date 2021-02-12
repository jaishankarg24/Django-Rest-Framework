from django.urls import path

from formapp import views

urlpatterns = [
	 path('display/', views.display_page),
	 path('register/', views.register_page),
	 path('thankyou/', views.thankyou_page),

]