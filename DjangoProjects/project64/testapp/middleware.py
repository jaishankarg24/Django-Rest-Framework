
class CustomMiddleware(object):

	def __init__(self, get_response):
		self.get_response= get_response

	def __call__(self, request):

		print('Message : PreProcessing  of Request')

		response=self.get_response(request)

		print('Messege : PostProcessing of Request  ')

		return response
