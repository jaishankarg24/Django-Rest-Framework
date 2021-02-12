from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first_app(request):
	data='<h1>Welcome to First Application</h1>'
	return HttpResponse(data)