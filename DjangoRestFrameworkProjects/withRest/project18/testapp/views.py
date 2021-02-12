from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.viewsets import *
from rest_framework.generics import ListAPIView
from testapp.pagination import Mypagination3

class EmployeeList(ListAPIView):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializer
	pagination_class=Mypagination3
	
