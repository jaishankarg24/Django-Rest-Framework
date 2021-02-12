from django.db import models

# Create your models here.

class CustomManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().order_by('eno')

	def get_emp_salary(self,sal1,sal2):
		return super().get_queryset().filter(esalary__range=(sal1,sal2))

class Employee(models.Model):
	eno = models.IntegerField()
	ename = models.CharField( max_length=50)
	esalary = models.FloatField()
	eaddress = models.CharField(max_length=100)
	obj=CustomManager()
