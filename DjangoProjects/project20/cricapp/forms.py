from django import forms

class Cricketer(forms.Form):
    # TODO: Define form fields here
    name = forms.CharField( max_length=50)
    dob = forms.DateField()
    address = forms.CharField( max_length=50)
    country = forms.CharField( max_length=50)
    role = forms.CharField( max_length=50)
    runs = forms.IntegerField()
    matches = forms.IntegerField()
    rank = forms.IntegerField()

    