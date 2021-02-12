from django.shortcuts import render

# Create your views here.
from myapp.forms import MyappForm

def name(request):
	form=MyappForm()
	my_dict={'form': form}
	return render(request=request, template_name='myapp/name.html', context=my_dict)

def age(request):
	form=MyappForm()
	name = request.GET['name']
	my_dict={'form': form, 'name':name}
	response=render(request=request, template_name='myapp/age.html', context=my_dict)
	response.set_cookie('name', name)
	return response

def girlfriend(request):
	form=MyappForm()
	name = request.COOKIES['name']
	age = request.GET['age']
	my_dict={'form':form, 'name':name, 'age':age}
	response=render(request=request, template_name='myapp/girlfriend.html', context=my_dict)
	response.set_cookie('age',age)
	return response

def result(request):
	name =request.COOKIES['name']
	age =request.COOKIES['age']
	girlfriend=request.GET['girlfriend']

	my_dict={'name':name, 'age':age, 'girlfriend':girlfriend}

	if request.method=='GET':
		gfdata=MyappForm(request.GET)

		if gfdata.is_valid():
			print(f'Girl friend name is: {gfdata.cleaned_data["girlfriend"]}')



	return render(request=request, template_name='myapp/result.html', context=my_dict)




