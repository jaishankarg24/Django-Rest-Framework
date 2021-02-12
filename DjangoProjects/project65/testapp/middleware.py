from django.http import HttpResponse

class ServerUnderMaintainance(object):

	def __init__(self, get_response):
		self.get_response= get_response

	def __call__(self, request):

		

		s = '<h1>Server is under Maintainance</h1><br> <h2>We will be back soon.</h2>'

	

		return HttpResponse(s)
