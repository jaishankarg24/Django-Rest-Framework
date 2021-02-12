from django.contrib import admin

# Register your models here.
from sqlapp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):

	list_display=('name', 'age','address', 'salary')


admin.site.register(Employee, EmployeeAdmin)