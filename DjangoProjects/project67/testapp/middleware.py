
from django.http import HttpResponse

class FirstMiddleware(object):
	def __init__(self,get_response):
		self.get_response = get_response

	def __call__(self,request):
		print('This line represents the Preprocessing request from FirstMiddleware')
		response = self.get_response(request)
		print('This line represents the postprocessing of response from FirstMiddleware')
		return response

class SecondMiddleware(object):
	def __init__(self,get_response):
		self.get_response = get_response

	def __call__(self,request):
		print('This line represents the Preprocessing request from SecondMiddleware')
		response = self.get_response(request)
		print('This line represents the postprocessing of response from SecondMiddleware')
		return response