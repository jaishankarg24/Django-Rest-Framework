from django.contrib import admin

# Register your models here.
from testapp.models import Books

class BooksAdmin(admin.ModelAdmin):
	list_display=['title','price']

admin.site.register(Books, BooksAdmin)