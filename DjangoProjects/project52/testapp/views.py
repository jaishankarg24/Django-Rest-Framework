from django.shortcuts import render

# Create your views here.
from testapp.models import Book
from django.views.generic import ListView,DetailView

class BookList(ListView):
	model=Book

class BookDetail(DetailView):
	model=Book