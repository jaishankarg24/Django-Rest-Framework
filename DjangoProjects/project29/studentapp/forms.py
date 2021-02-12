from django import forms

from django.core import validators

class StudentForm(forms.Form):
	name = forms.CharField( max_length=50)
	mail_id = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)
	re_password = forms.CharField(label='Password(Again)',widget=forms.PasswordInput)
	trainer_name = forms.CharField()
	feedback = forms.CharField(widget=forms.Textarea)
	bot_handler = forms.CharField(required=False,widget=forms.HiddenInput)


	def clean(self):

		print('complete validation using single clean method')
		total_cleaned_data=super().clean()

		input_name=total_cleaned_data['name']
		if len(input_name)<4:
			raise forms.ValidationError('Name should be greater than 4 characters')


		input_trainer_name=total_cleaned_data['trainer_name']
		if input_trainer_name[0].lower()!='s':
			raise forms.ValidationError('Trainer name should start with s or S letter')
		
		input_password=total_cleaned_data['password']
		input_re_password=total_cleaned_data['re_password']
		if input_password!=input_re_password:
			raise forms.ValidationError('Password Mismatch!!!!')

		input_bot_handler=total_cleaned_data['bot_handler']
		if len(input_bot_handler)>0:
			raise forms.ValidationError('Thanks BOT...do not try to automate !!!!')