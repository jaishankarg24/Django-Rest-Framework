from shimogaapp import views as shimoga
from django.urls import path
urlpatterns = [
    path('shimoga/ravindranagar', shimoga.ravindranagar_cases),
    path('shimoga/gopala', shimoga.gopala_cases),
    path('shimoga/bapujinagar', shimoga.bapujinagar_cases),
]