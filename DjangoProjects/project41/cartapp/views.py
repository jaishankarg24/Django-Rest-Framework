from django.shortcuts import render
from cartapp.forms import Product

# Create your views here.
def homepage(request):
	return render(request=request, template_name='cartapp/homepage.html')

def addproduct(request):
	form = Product()

	if request.method =='POST':

		name=request.POST['name']
		quantity=request.POST['quantity']

		request.session[name]=quantity

	my_dict={'form':form}
	return render(request=request, template_name='cartapp/addproduct.html', context=my_dict)

def cart(request):
	return render(request=request, template_name='cartapp/cart.html')