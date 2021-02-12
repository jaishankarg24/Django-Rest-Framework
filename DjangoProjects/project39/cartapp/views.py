from django.shortcuts import render
from cartapp.forms import Product

# Create your views here.
def homepage(request):
	return render(request=request, template_name='cartapp/homepage.html')

def addproduct(request):
	form = Product()
	my_dict = {'form':form}

	response=render(request=request, template_name='cartapp/addproduct.html', context=my_dict)

	if request.method =='POST':
		data=Product(request.POST)
		if data.is_valid():
			name=data.cleaned_data['name']
			quantity=data.cleaned_data['quantity']

			response.set_cookie(name,quantity,300)

	return response

def cart(request):
	return render(request=request, template_name='cartapp/cart.html')