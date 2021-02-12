from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def vijaynagar_cases(request):
	data='<h1>Total Number of Corona Active Cases in vijaynagar/Bengaluru: 500</h1>'
	return HttpResponse(data)


def btm_cases(request):
	data='<h1>Total Number of Corona Active Cases in btm/Bengaluru: 1000</h1>'
	return HttpResponse(data)


def hebbal_cases(request):
	data='<h1>Total Number of Corona Active Cases in hebbal/Bengaluru: 300</h1>'
	return HttpResponse(data)