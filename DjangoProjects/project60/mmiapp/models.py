from django.db import models
class Parent1(models.Model):
	p1_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	dob = models.CharField(max_length=50)

class Parent2(models.Model):
	p2_id = models.AutoField(primary_key=True)
	eno = models.IntegerField()
	esalary = models.IntegerField()
	
class Child(Parent1,Parent2):
	no_of_projects = models.IntegerField()
	