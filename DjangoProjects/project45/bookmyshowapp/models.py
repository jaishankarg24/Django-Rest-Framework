from django.db import models

# Create your models here.
class Movie(models.Model):
	name = models.CharField( max_length=50)
	hero = models.CharField(max_length=50) 
	heroine = models.CharField( max_length=50)
	director = models.CharField( max_length=50)
	release_date = models.DateField()
	language = models.CharField( max_length=50)
	rating = models.IntegerField()