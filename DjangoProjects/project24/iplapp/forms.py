from django import forms

from iplapp.models import IplTable

class IplTableForm(forms.ModelForm):

	class Meta:
		model = IplTable
		fields = ('name','age', 'country')

		
