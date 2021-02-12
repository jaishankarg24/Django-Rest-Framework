from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.generics import *


class EmployeeListModelMixin(mixins.CreateModelMixin,mixins.ListModelMixin):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializer
	def list(self,request,*args,**kwargs):
		return self.list(request,*args,**kwargs)
	def post(self,request,*args,**kwargs):
		return self.create(request,*args,**kwargs)

class EmployeeDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializer
	def put(self,request,*args,**kwargs):
		return self.update(request,*args,**kwargs)

	def patch(self,request,*args,**kwargs):
		return self.partial_update(request,*args,**kwargs)

	def delete(self,request,*args,**kwargs):
		return self.destroy(request,*args,**kwargs)
