from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import datetime

def welcom_clients(request):

	date=datetime.datetime.now()
	hour=int(datetime.datetime.now().hour)
	msg='<h1> Hi Students Good '
	if hour>0 and hour<12:
		msg=msg+'<h1>Morning</h1>'
	elif hour>12 and hour<16:
		msg=msg+'<h1>Afternoon</h1>'
	elif hour>=16 and hour<21:
		msg=msg+'<h1>Evening</h1>'
	else:
		msg=msg+'<h1>Night</h1>'

	msg=msg+'</h1><hr>'

	msg=msg+'<h1>The Current Server Time is :'+str(date)+'</h1>'

	return HttpResponse(msg)