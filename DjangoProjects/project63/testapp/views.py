from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def middleware_check(request):
	name=request.user
	print(name)

	response='''
			<html>
				<head>
					<title>Django MiddleWare</title>
				</head>
				<body>
					<h1> This is the Response from server with default django middleware.</h1>
				</body>
			</html>
			'''
	return HttpResponse(response)