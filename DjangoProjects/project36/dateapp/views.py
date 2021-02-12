from django.shortcuts import render

# Create your views here.
from dateapp.forms import UserForm

def home_page(request):
	form = UserForm()
	my_dict={'form':form}
	return render(request=request, template_name='dateapp/homepage.html', context=my_dict)


def collect_cookie(request):
	name=request.GET['name']
	my_dict={'name':name}

	response=render(request=request, template_name='dateapp/collectcookie.html', context=my_dict)

	response.set_cookie('name', name)
	return response

import datetime
def display_date(request):
	date=datetime.datetime.now()
	name=request.COOKIES['name']
	my_dict={'name':name, 'date':date}

	return render(request=request, template_name='dateapp/displaydate.html', context=my_dict)
