from django.http import HttpResponse

class ErrorMessageMiddleware(object):

	def __init__(self, get_response):
		self.get_response= get_response

	def __call__(self, request):
		print('Preprocessing request')
		response=self.get_response(request)
		return response

	def process_exception(self, request, exception):
		s1='<h1>Currenlty there is a bug in server</h1> <hr>'
		s2='<h2>Raised Exception:{}</h2>'.format(exception.__class__.__name__)
		s3='<h2>Exception Meassge:{}</h2>'.format(exception)
		return HttpResponse(s1+s2+s3)

