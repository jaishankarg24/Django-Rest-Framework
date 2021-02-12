from django import forms


class Student(forms.Form):
    # TODO: Define form fields here
    name = forms.CharField( max_length=50)
    age = forms.IntegerField()
    address = forms.CharField( max_length=50)