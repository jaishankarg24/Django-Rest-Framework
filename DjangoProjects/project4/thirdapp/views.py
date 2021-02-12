from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def third_app(request):
	data='<h1>Welcome to Third Application</h1>'
	return HttpResponse(data)