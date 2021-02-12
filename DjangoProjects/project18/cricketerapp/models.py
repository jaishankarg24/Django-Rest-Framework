from django.db import models

# Create your models here.

class Cricketer(models.Model):
	name = models.CharField( max_length=50)
	dob = models.DateField()
	address = models.CharField( max_length=50)
	department = models.CharField( max_length=50)


	def __str__(self):
		return self.name
