from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def welcome(request):
	print('This line is getting printed while processing the request')
	s='<h1>Multiple middleware application</h1>'
	return HttpResponse(s)