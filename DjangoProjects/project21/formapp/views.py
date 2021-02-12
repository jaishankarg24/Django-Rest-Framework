from django.shortcuts import render

# Create your views here.
from formapp.forms import Student

def display_page(request):
	return render(request=request, template_name='formapp/display.html') 

def thankyou_page(request):
	return render(request=request, template_name='formapp/thankyou.html')

def register_page(request):
	if request.method=='GET':
		form = Student()
		my_dict={'form':form}

		return render(request=request, template_name='formapp/register.html', context=my_dict)

	if request.method=='POST':
		form_data=Student(request.POST)
		my_dict={'form_data':form_data}

		if form_data.is_valid():
			print('Data Entered by the user:')
			print('Name:', form_data.cleaned_data['name'])
			print('PASSWORD:', form_data.cleaned_data['password'])
			print('RePassword:', form_data.cleaned_data['repassword'])
			print('DATE:', form_data.cleaned_data['date'])
			print('studyonlineid:', form_data.cleaned_data['studyonlineid'])
			print('phno:', form_data.cleaned_data['phno'])
			print('feedback:', form_data.cleaned_data['feedback'])

			return thankyou_page(request)

	return render(request=request, template_name='formapp/register.html', context=my_dict)
