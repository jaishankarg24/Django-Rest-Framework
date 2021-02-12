from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def welcome(request):
	return render(request=request, template_name='greetingapp/display.html')
