from django.shortcuts import render

# Create your views here.

from templatefilterapp.models import FilterModel

def upper_info(request):
	data=FilterModel.objects.all()
	my_dict={'data':data}
	return render(request=request, template_name='templatefilterapp/upper.html', context=my_dict)

def lower_info(request):
	data=FilterModel.objects.all()
	my_dict={'data':data}
	return render(request=request, template_name='templatefilterapp/lower.html', context=my_dict)
