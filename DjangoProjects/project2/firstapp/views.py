from django.shortcuts import render

# Create your views here.
import datetime
from django.http import HttpResponse

def Welcome_clients(request):

	date=datetime.datetime.now()

	msg1='<h1>Welcome Clients  </h1>'
	msg2=msg1+'<h1>The Current Server time is :'+str(date)+' </h1>'
	return HttpResponse(msg2)
