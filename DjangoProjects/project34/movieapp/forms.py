from django import forms

from movieapp.models import MoviesTable

class MovieTableForm(forms.ModelForm):
	class Meta:
		model = MoviesTable
		fields = ('name', 'releasedate', 'hero', 'heroine', 'director', 'budget', 'language', 'rating')

