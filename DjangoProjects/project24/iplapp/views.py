from django.shortcuts import render

# Create your views here.
from iplapp.forms import IplTableForm

def display_page(request):
	return render(request=request, template_name='iplapp/display.html')


def addplayer(request):
	form = IplTableForm()
	my_dict = {'form': form}

	if request.method=='POST':
		data_form = IplTableForm(request.POST)
		my_dict = {'data_form': data_form}

		if data_form.is_valid():
			data_form.save(commit=True)

	if request.method=='POST':
		form_data = IplTableForm(request.POST)
		my_dict = {'form_data': form_data}

		if form_data.is_valid():
			print('Entered Details')
			print(f'Name:{form_data.cleaned_data["name"]}')
			print(f'Age:{form_data.cleaned_data["age"]}')
			print(f'Country:{form_data.cleaned_data["country"]}')




	return render(request=request, template_name='iplapp/addplayer.html', context=my_dict)


from iplapp.models import IplTable

def playerlist(request):
	data_table = IplTable.objects.all()

	my_dict={'data_table': data_table}

	return render(request=request, template_name='iplapp/playerlist.html', context=my_dict)
