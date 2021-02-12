from django.shortcuts import render

# Create your views here.
def count(request):
	count=request.session.get('count',0)
	newcount=count+1
	my_dict={'count':newcount}
	request.session['count']=newcount
	print('Expiry date:', request.session.get_expiry_date())

	return render(request=request, template_name='sessionapiapp/count.html', context=my_dict)