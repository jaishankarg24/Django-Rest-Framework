from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def ravindranagar_cases(request):
	data='<h1>Total Number of Corona Active Cases in ravindraNagar/shimoga: 300</h1>'
	return HttpResponse(data)

def gopala_cases(request):
	data='<h1>Total Number of Corona Active Cases in GopalaNagar/shimoga: 240</h1>'
	return HttpResponse(data)

def bapujinagar_cases(request):
	data='<h1>Total Number of Corona Active Cases in bapujiNagar/shimoga: 200</h1>'
	return HttpResponse(data)