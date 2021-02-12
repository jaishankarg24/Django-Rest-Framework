from django.shortcuts import render

# Create your views here.
from usertemplatefilterapp.models import UserFilter

def user_filter(request):
	data=UserFilter.objects.all()
	my_dict= {'data': data}

	return render(request=request, template_name='usertemplatefilterapp/usertemplatefilterapp.html', context=my_dict)