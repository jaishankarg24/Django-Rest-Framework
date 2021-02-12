from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
from django.http import HttpResponse
import json
# Create your views here.
# class EmployeeDetailsCbv(View):
# 	def get(self,request,*args,**kwargs):
# 		emp=Employee.objects.get(id=1)
# 		print(emp)
# 		print(type(emp))

# 		emp_data={
# 			'eno':emp.eno,
# 			'ename':emp.ename,
# 			'esalary':emp.esalary,
# 			'eaddress':emp.eaddress
# 		}
# 		json_data=json.dumps(emp_data)
# 		return HttpResponse(json_data,content_type='application/json')


#Dynamically taking the input from user
class EmployeeDetailsCbv(View):
	def get(self,request,id,*args,**kwargs):
		emp=Employee.objects.get(id=id)
		print(emp)
		print(type(emp))
		
		emp_data={
			'eno':emp.eno,
			'ename':emp.ename,
			'esalary':emp.esalary,
			'eaddress':emp.eaddress
		}
		json_data=json.dumps(emp_data)
		return HttpResponse(json_data,content_type='application/json')