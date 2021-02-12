from django.shortcuts import render

from django.http import JsonResponse

from django.views.generic import View

class CbvJsonResponse(View):
	def get(self, request, *args, **kwargs):
		data={'eno':4, 'ename': 'jaishankar_g', 'eage':23, 'eaddress':'shivamogga'}
		
		return JsonResponse(data)