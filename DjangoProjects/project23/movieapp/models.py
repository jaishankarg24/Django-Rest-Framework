from django.db import models

# Create your models here.

class MoviesTable(models.Model):
	name = models.CharField( max_length=50)
	releasedate = models.DateField()
	hero = models.CharField(max_length=50)
	heroine = models.CharField( max_length=50)
	director = models.CharField( max_length=50)
	language = models.CharField( max_length=50)
	budget = models.IntegerField()
	rating = models.IntegerField()
