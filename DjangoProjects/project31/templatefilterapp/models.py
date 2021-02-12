from django.db import models

# Create your models here.

class FilterModel(models.Model):
	name = models.CharField( max_length=50)
	age = models.IntegerField()
	department = models.CharField( max_length=50)
	date = models.DateField()
