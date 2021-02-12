from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

#Class Based View

class Welcome(TemplateView):
	template_name='cbvapp/display.html'