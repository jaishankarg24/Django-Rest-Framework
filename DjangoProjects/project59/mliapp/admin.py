from django.contrib import admin

# Register your models here.
from mliapp.models import *

admin.site.register(Person)
admin.site.register(Employee)
admin.site.register(Manager)