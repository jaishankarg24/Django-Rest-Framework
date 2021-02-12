from django.db import models

# Create your models here.
class IplTable(models.Model):
	name = models.CharField( max_length=50)
	age = models.IntegerField()
	country = models.CharField( max_length=50)