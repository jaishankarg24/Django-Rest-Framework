from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.viewsets import *
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from testapp.authentications import CustomAuthentication1,CustomAuthentication2

class EmployeeCRUD(ModelViewSet):
	serializer_class=EmployeeSerializer
	queryset=Employee.objects.all()

	#locally enabled
	authentication_classes=[CustomAuthentication2,]
	permission_classes= [IsAuthenticated,]