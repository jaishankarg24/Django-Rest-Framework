from django.shortcuts import render

# Create your views here.
from datetime import datetime

def display_time(request):
	server_time=datetime.now()
	msg={'time':server_time}
	return render(request=request, template_name='displaytime/time.html', context=msg)
	