from django.shortcuts import render

# Create your views here.
from testapp.models import Book
from django.views.generic import ListView


def display_fbv(request):
	fbook=Book.objects.all()
	my_dict={'fbook':fbook}
	return render(request=request, template_name='testapp/displayfbv.html', context=my_dict)


class BookClass(ListView):
	model=Book