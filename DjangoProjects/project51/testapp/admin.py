from django.contrib import admin

# Register your models here.
from testapp.models import Book

class BookAdmin(admin.ModelAdmin):
	list_display=['title','price']

admin.site.register(Book, BookAdmin)