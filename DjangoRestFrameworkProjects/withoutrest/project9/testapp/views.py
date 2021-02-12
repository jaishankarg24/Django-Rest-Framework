from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
from django.http import HttpResponse
import json
from django.core.serializers import serialize
 
class CompleteEmployeeDetailsCbv(View):
	def get(self,request,*args,**kwargs):
		emp_query_set=Employee.objects.all()
		json_data = serialize('json',emp_query_set)
		return HttpResponse(json_data,content_type='application/json')