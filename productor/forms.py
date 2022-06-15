from django import forms

class Productor(forms.Form):
    name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    cuil = forms.IntegerField()
    email = forms.EmailField()