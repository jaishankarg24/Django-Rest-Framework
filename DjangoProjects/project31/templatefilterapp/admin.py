from django.contrib import admin

# Register your models here.

from templatefilterapp.models import FilterModel

class AdminFilterModel(admin.ModelAdmin):
	list_display=['name','age','department','date']

admin.site.register(FilterModel, AdminFilterModel)
