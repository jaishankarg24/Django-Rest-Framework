from django.shortcuts import render

# Create your views here.
from testapp.models import Books
from django.views.generic import ListView

class DisplayCbv(ListView):
	model=Books

	template_name='testapp/display.html'

	context_object_name='list_of_books'