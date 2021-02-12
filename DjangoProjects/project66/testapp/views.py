from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def welcome(request):
	print('Message : This Message execute while process the request')
	print(10/0)
	response='<h1> Welcome : This is CustomMiddleware </h1>'
	return HttpResponse(response)