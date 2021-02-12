from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json

def json_data(request):
	data={'eno':4, 'ename': 'jaishankar_g', 'eage':23, 'eaddress':'shivamogga'}
	response=json.dumps(data)
	return HttpResponse(response, content_type ='application/json')

from django.http import JsonResponse

def json_response(request):
	data={'eno':4, 'ename': 'jaishankar_g', 'eage':23, 'eaddress':'shivamogga'}
	response=data
	return JsonResponse(response)