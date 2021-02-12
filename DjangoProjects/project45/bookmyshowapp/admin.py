from django.contrib import admin

from bookmyshowapp.models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):

	list_display=['name', 'hero', 'heroine','director']

admin.site.register(Movie, MovieAdmin)