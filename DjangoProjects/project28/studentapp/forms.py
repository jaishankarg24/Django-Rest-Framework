from django import forms

from django.core import validators

class StudentForm(forms.Form):
	name = forms.CharField( max_length=50)
	mail_id = forms.EmailField()
	trainer_name = forms.CharField()
	feedback = forms.CharField(widget=forms.Textarea)


	def clean(self):

		print('complete validation using single clean method')
		total_cleaned_data=super().clean()

		input_name=total_cleaned_data['name']
		if len(input_name)<4:
			raise forms.ValidationError('Name should be greater then 4 characters')


		input_trainer_name=total_cleaned_data['trainer_name']
		if input_trainer_name[0].lower()!='s':
			raise forms.ValidationError('Trainer name should start with s or S letter')