from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField( max_length=50)
	dob = models.DateField()
	branch = models.CharField( max_length=50)
	phone = models.CharField( max_length=50)
	email = models.EmailField()
	course = models.CharField( max_length=50)
	address = models.CharField( max_length=50)

	def __str__(self):
		return self.name