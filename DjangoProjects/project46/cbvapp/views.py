from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.

#Class Based View

class Welcome(View):
	def get(self,request):
		data='<h1>Welcome to Study Online. This is from View Class</h1>'
		return HttpResponse(data)