from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
from django.http import HttpResponse
import json
from django.core.serializers import serialize
#Dynamically taking the input from user
class EmployeeDetailsCbv(View):
	def get(self,request,id,*args,**kwargs):
		emp=Employee.objects.get(id=id)

		# serialize(format,queryset,fields)
		json_data=serialize('json',[emp,],fields=('eno','ename'))
		return HttpResponse(json_data,content_type='application/json')