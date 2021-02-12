from django.shortcuts import render, redirect
from mmapp.models import *
from django.db.models import *

# Create your views here.
def retrieve_data(request):
	# emp=Employee.objects.all()
	# emp=ProxyEmployee1.objects.all()
	emp=ProxyEmployee2.objects.all()
	my_dict={'emp':emp}
	return render(request=request, template_name='display.html',context=my_dict)




