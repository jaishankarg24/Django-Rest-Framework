from django.contrib import admin

# Register your models here.
from crudapp.models import Company

class CompanyAdmin(admin.ModelAdmin):
	list_display=['name','location','ceo']

admin.site.register(Company, CompanyAdmin)