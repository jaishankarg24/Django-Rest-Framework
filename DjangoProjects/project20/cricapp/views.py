from django.shortcuts import render

# Create your views here.

from cricapp.forms import Cricketer

def cricketer_form(request):

	form=Cricketer()
	my_dict={'form':form}

	return render(request=request, template_name='cricapp/display.html', context=my_dict)
