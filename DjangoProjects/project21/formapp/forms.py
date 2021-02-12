from django import forms

class Student(forms.Form):
    # TODO: Define form fields here

    name = forms.CharField()
    password = forms.CharField()
    repassword = forms.CharField()
    date = forms.DateField()
    studyonlineid = forms.CharField()
    phno = forms.CharField()
    feedback = forms.CharField(widget=forms.Textarea)
