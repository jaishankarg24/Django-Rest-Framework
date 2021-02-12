from django.urls import path

from studentdetailapp import views as v

urlpatterns =[
	 path('home/', v.display_homepage),
	 path('studentdetails/', v.display_studentdetails),
]