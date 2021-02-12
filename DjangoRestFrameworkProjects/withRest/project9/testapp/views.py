from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.generics import *


class EmployeeListCreateAPIView(ListCreateAPIView):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializer

# class EmployeeDetailUpdateAPIView(RetrieveUpdateAPIView):
# 	queryset=Employee.objects.all()
# 	serializer_class=EmployeeSerializer
# 	lookup_field='id'

# class EmployeeDetailDeleteAPIView(RetrieveDestroyAPIView):
# 	queryset=Employee.objects.all()
# 	serializer_class=EmployeeSerializer

class EmployeeDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializer