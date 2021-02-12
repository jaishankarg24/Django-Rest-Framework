from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.viewsets import *


class EmployeeCRUD(ModelViewSet):
	serializer_class=EmployeeSerializer
	queryset=Employee.objects.all()
