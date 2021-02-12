from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.viewsets import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

class EmployeeCRUD(ModelViewSet):
	serializer_class=EmployeeSerializer
	queryset=Employee.objects.all()

	#locally enabled
	authentication_classes=[TokenAuthentication,]
	permission_classes=[DjangoModelPermissionsOrAnonReadOnly,]
