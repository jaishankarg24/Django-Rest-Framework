from django.db import models

# Create your models here.
class ContactInfo(models.Model):
	name = models.CharField( max_length=50)
	email = models.EmailField()
	address = models.CharField(max_length=50)


class Student(ContactInfo):
	rollno = models.IntegerField()
	marks = models.IntegerField()

class Teacher(ContactInfo):
	subject = models.IntegerField()
	salary = models.IntegerField()



