from django.shortcuts import render, redirect
from mmapp.models import *
from django.db.models import *

# Create your views here.
def retrieve_data(request):
	#emp=Employee.obj.all()
	emp=Employee.obj.get_emp_salary(200000, 300000)
	my_dict={'emp':emp}
	return render(request=request, template_name='display.html',context=my_dict)




