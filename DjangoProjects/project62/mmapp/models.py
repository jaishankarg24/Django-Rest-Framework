from django.db import models

# Create your models here.

class CustomManager1(models.Manager):
	def get_queryset(self):
		return super().get_queryset().order_by('eno')

class CustomManager2(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(esalary__gt=200000)

class CustomManager3(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(esalary__lt=200000)


class Employee(models.Model):
	eno = models.IntegerField()
	ename = models.CharField( max_length=50)
	esalary = models.FloatField()
	eaddress = models.CharField(max_length=100)
	objects=CustomManager1()

class ProxyEmployee1(Employee):
	objects=CustomManager2()
	class Meta:
		proxy=True

class ProxyEmployee2(Employee):
	objects=CustomManager3()
	class Meta:
		proxy=True
