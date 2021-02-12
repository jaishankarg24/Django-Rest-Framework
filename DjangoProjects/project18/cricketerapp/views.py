from django.shortcuts import render

# Create your views here.

from cricketerapp.models import Cricketer

def display_homepage(request):
	return render(request=request, template_name='cricketerapp/homepage.html')

def display_cricketers(request):

	cricketer_data = Cricketer.objects.all()

	my_dict={'cricketer_data': cricketer_data}

	return render(request=request, template_name='cricketerapp/display.html', context=my_dict)
