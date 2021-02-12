from django.shortcuts import render,redirect
from crudapp.models import Employee
from crudapp.forms import EmployeeForm

from django.db.models import *

# Create your views here.

def homepage(request):
	return render(request=request, template_name='crudapp/home.html')

def aggregate(request):
	avg=Employee.objects.all().aggregate(Avg('esalary'))
	maximun=Employee.objects.all().aggregate(Max('esalary'))
	minimum=Employee.objects.all().aggregate(Min('esalary'))
	complete_salary=Employee.objects.all().aggregate(Sum('esalary'))
	count=Employee.objects.all().aggregate(Count('esalary'))
	
	my_dict={'avg':avg,'max':maximun,'min':minimum,'sum':complete_salary,'count':count}
	return render(request=request, template_name='crudapp/aggregate.html',context=my_dict)
	
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


