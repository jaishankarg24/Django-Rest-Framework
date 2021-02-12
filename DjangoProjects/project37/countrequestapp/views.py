from django.shortcuts import render

# Create your views here.

def home_page(request):
	count = int(request.COOKIES.get('count', 0))
	newcount = count+1
	my_dict={'newcount':newcount}
	response=render(request=request, template_name='countrequestapp/homepage.html', context=my_dict)
	response.set_cookie('count',newcount, max_age=60)
	return response

