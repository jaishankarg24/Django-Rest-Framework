from django.shortcuts import render

# Create your views here.
from testapp.models import Book
from django.views.generic import DetailView




class BookClass(DetailView):
	model=Book