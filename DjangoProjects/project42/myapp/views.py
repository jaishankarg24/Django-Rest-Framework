from django.shortcuts import render

# Create your views here.
from myapp.forms import MyappForm

def name(request):
	form=MyappForm()
	my_dict={'form': form}
	return render(request=request, template_name='myapp/name.html', context=my_dict)

def age(request):
	form=MyappForm()
	newname = request.GET['name']
	my_dict={'form': form, 'name':newname}
	request.session['name']=newname
	return render(request=request, template_name='myapp/age.html', context=my_dict)
	

def girlfriend(request):
	form=MyappForm()
	name = request.session['name']
	age = request.GET['age']
	my_dict={'form':form, 'name':name, 'age':age}
	request.session['age']=age
	return render(request=request, template_name='myapp/girlfriend.html', context=my_dict)
	

def result(request):
	name =request.session['name']
	age =request.session['age']
	girlfriend=request.GET['girlfriend']

	my_dict={'name':name, 'age':age, 'girlfriend':girlfriend}

	return render(request=request, template_name='myapp/result.html', context=my_dict)




