from django.shortcuts import render

# Create your views here.
from modelformapp.forms import StudentForm

def display_page(request):
	form = StudentForm()
	my_dict= {'form':form}


	if request.method=='POST':
		data_form = StudentForm(request.POST)

		if data_form.is_valid():
			print('Data successfully stored in the database')
			data_form.save(commit=True)

			print('Data enterted by End user:')
			print(data_form.cleaned_data)
			print(type(data_form.cleaned_data))
			print('Name of the Student:',data_form.cleaned_data['name'])
			print('Name of the Student:',data_form.cleaned_data['age'])
			print('Name of the Student:',data_form.cleaned_data['address'])

	return render(request=request, template_name='modelformapp/display.html', context=my_dict)

