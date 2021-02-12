from django.db import models

# Create your models here.

class UserFilter(models.Model):
	name = models.CharField( max_length=50)
	technology = models.CharField( max_length=50)
	trainer = models.CharField(max_length=50)