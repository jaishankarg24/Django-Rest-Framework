from django.shortcuts import render,redirect
from crudapp.models import Employee
from crudapp.forms import EmployeeForm
from django.db.models import *

# Create your views here.

def homepage(request):
	return render(request=request, template_name='crudapp/home.html')

def home(request):
	return render(request=request, template_name='crudapp/homepage.html')

def or_p(request):
	emp=Employee.objects.filter(ename__startswith='s')|Employee.objects.filter(esalary__range=(100000, 250000))
	my_dict={'emp':emp}
	return render(request=request, template_name='crudapp/or.html', context=my_dict)
	
def and_p(request):
	emp=Employee.objects.filter(ename__startswith='j', esalary__gt=100000)
	my_dict={'emp':emp}
	return render(request=request, template_name='crudapp/and.html', context=my_dict)

def not_p(request):
	emp=Employee.objects.filter(~Q(ename__startswith='w'))
	my_dict={'emp':emp}
	return render(request=request, template_name='crudapp/not.html', context=my_dict)

def retrieve_data(request):
	emp=Employee.objects.all()
	#emp=Employee.objects.filter(esalary__gt=250000)
	#emp=Employee.objects.filter(id__exact=11)
	#emp=Employee.objects.get(id__exact=11)


	my_dict={'emp':emp}
	return render(request=request, template_name='crudapp/display.html',context=my_dict)

def create_data(request):
	form=EmployeeForm()
	my_dict={'form':form}
	if request.method=='POST':
		form=EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/display/')	

	return render(request=request, template_name='crudapp/create.html',context=my_dict)

def delete_view(request,id):
	employee=Employee.objects.get(id=id)
	employee.delete()
	return redirect('/display/')	

def update_view(request,id):
	employee=Employee.objects.get(id=id)
	my_dict={'employee':employee}
	if request.method=="POST":
		form=EmployeeForm(request.POST,instance=employee)
		if form.is_valid():
			form.save()
		return redirect('/display/')
	return render(request=request, template_name='crudapp/update.html',context=my_dict)


