from django import forms

from django.core import validators

class StudentForm(forms.Form):
	name = forms.CharField( max_length=50)
	mail_id = forms.EmailField()
	feedback = forms.CharField(widget=forms.Textarea, validators=[validators.MinLengthValidator(4), validators.MaxLengthValidator(20)])