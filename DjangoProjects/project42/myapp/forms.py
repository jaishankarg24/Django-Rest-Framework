from django import forms

class MyappForm(forms.Form):
	name = forms.CharField()
	age = forms.IntegerField()
	girlfriend = forms.CharField()