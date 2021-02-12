from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def second_app(request):
	data='<h1>Welcome to Second Application</h1>'
	return HttpResponse(data)