from django.contrib import admin
from usertemplatefilterapp.models import UserFilter
# Register your models here.

class UserFilterAdmin(admin.ModelAdmin):
	list_display=['name','technology', 'trainer']


admin.site.register(UserFilter, UserFilterAdmin)