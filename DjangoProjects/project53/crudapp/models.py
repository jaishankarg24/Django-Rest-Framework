from django.db import models

# Create your models here.
from django.urls import reverse

class Company(models.Model):
	name = models.CharField( max_length=50)
	location = models.CharField( max_length=50)
	ceo = models.CharField( max_length=50)

	def get_absolute_url(self):
		return reverse('detail',kwargs={'pk':self.pk})