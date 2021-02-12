from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
from django.http import HttpResponse
import json
# from django.core.serializers import serialize
from testapp.mixins import SerializeMixin

class CompleteEmployeeDetailsCbv(SerializeMixin,View):
	def get(self,request,*args,**kwargs):
		qs=Employee.objects.all()
		json_data = self.serialize(qs)
		return HttpResponse(json_data,content_type='application/json')