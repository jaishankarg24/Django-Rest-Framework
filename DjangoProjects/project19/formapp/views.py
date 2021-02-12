from django.shortcuts import render

# Create your views here.
from formapp.forms import Student

def student_form(request):
	form = Student()

	my_dict = {'form':form} 

	return render(request=request, template_name='formapp/display.html', context=my_dict)