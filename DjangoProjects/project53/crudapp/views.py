from django.shortcuts import render

# Create your views here.
from crudapp.models import Company

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView
from django.urls import reverse_lazy

class CompanyHome(TemplateView):
	template_name='crudapp/home.html'

class CompanyListview(ListView):
	model=Company

class CompanyDetailView(DetailView):
	model=Company

class CompanyCreateView(CreateView):
	model=Company
	fields=['name','location','ceo']

class CompanyUpdateView(UpdateView):
	model=Company
	fields=['name','location','ceo']

class CompanyDeleteView(DeleteView):
	model=Company
	fields=['name','location','ceo']
	success_url=reverse_lazy('companylist')