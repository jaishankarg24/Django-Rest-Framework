from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

#Class Based View

class Student(TemplateView):
	template_name='cbvapp/display.html'

	def get_context_data(self,**kwargs):
		context=super().get_context_data(**kwargs)
		context['name']='jaishankar g'
		context['subject']='Python'
		context['marks']=90
		return context
