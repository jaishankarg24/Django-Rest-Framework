from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def ramakrishnanagar_cases(request):
	data='<h1>Total Number of Corona Active Cases in ramakrishnaNagar/Mysore: 390</h1>'
	return HttpResponse(data)


def basavanagudi_cases(request):
	data='<h1>Total Number of Corona Active Cases in basavanagudi/Mysore: 600</h1>'
	return HttpResponse(data)


def vijaynagar_cases(request):
	data='<h1>Total Number of Corona Active Cases vijaynagar/Mysore: 450</h1>'
	return HttpResponse(data)