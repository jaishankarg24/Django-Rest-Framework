from django import forms

class StudentForm(forms.Form):
	name = forms.CharField( max_length=50)
	mail_id = forms.EmailField()
	feedback = forms.CharField(widget=forms.Textarea)


	def clean_name(self):
		input_name = self.cleaned_data['name']
		print('validating name field')
		if len(input_name)<=3:
			raise forms.ValidationError('name must be greater then 3 characters')

		return input_name

	def clean_mail_id(self):
		input_mailid = self.cleaned_data['mail_id']
		print('validating email field')
		return input_mailid


	def clean_feedback(self):
		input_feedback = self.cleaned_data['feedback']
		print('validating feedback field')
		return input_feedback