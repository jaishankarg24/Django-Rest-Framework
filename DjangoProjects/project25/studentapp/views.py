from django.shortcuts import render
from studentapp.forms import StudentForm
# Create your views here.

def home_page(request):
	return render(request=request, template_name='studentapp/homepage.html')

def thankyou(request):
	return render(request=request, template_name='studentapp/thankyou.html')

def feedback(request):

	if request.method=='GET':
		form = StudentForm()
		my_dict = {'form': form}

	if request.method=='POST':
		form = StudentForm(request.POST)
		my_dict= {'form' : form}

		if form.is_valid():
			print('Details of Entered information is')

			print(f'Name:{form.cleaned_data["name"]}')
			print(f'Email:{form.cleaned_data["mail_id"]}')
			print(f'Feedback:{form.cleaned_data["feedback"]}')
			print('Complete data is validated using clean_fieldname()')

			return thankyou(request)

	return render(request=request, template_name='studentapp/feedback.html', context=my_dict)
