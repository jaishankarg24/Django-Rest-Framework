from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def display_data(request):
	data='<marquee style ="color:red" direction="Right">Welcome to learn Django and REST API by SANDESH</marquee>'
	return HttpResponse(data)
