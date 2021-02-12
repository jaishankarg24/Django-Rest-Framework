from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
from django.http import HttpResponse
import json
# from django.core.serializers import serialize
from testapp.mixins import SerializeMixin

class EmployeeDetailsCbv(SerializeMixin,View):
	def get(self,request,id,*args,**kwargs):
		try:
			qs=Employee.objects.get(id=id)
		except Employee.DoesNotExist:
			json_data = json.dumps({'msg':'The required source is not available'})
		else:
			json_data = self.serialize([qs,])

		return HttpResponse(json_data,content_type='application/json')

# Writing the Error code in Partner application
class EmployeedetailsCbv(SerializeMixin,View):
	def get(self,request,id,*args,**kwargs):
		qs=Employee.objects.get(id=id)
		json_data = self.serialize([qs,])

		return HttpResponse(json_data,content_type='application/json')