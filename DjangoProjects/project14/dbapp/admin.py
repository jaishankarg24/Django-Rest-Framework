from django.contrib import admin

# Register your models here.
from dbapp.models import Student

class StudentAdmin(admin.ModelAdmin):
	list_display=('name', 'age', 'address')

admin.site.register(Student, StudentAdmin)