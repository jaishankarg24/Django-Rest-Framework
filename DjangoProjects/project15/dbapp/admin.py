from django.contrib import admin

# Register your models here.
from dbapp.models import Cricketer

class RegCricketer(admin.ModelAdmin):
	list_display= ('name', 'country')

admin.site.register(Cricketer, RegCricketer)