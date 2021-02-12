from django.urls import path

from cricketerapp import views as v

urlpatterns = [
	path('home/', v.display_homepage),
	path('cricketerdetails/', v.display_cricketers),
]