from django import forms

from django.core import validators

def trainer_name(data):
	if data[0].lower()!='s':
		raise forms.ValidationError('Trainer name should start with s or S letter')

class StudentForm(forms.Form):
	name = forms.CharField( max_length=50)
	mail_id = forms.EmailField()

	trainer_name = forms.CharField(validators=[trainer_name])

	feedback = forms.CharField(widget=forms.Textarea)