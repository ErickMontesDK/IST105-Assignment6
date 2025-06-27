from django import forms

class NumbersForm(forms.Form):
    numberA = forms.IntegerField(label='Number A', min_value=0)
    numberB = forms.IntegerField(label='Number B', min_value=0)
    numberC = forms.IntegerField(label='Number C', min_value=0)
    numberD = forms.IntegerField(label='Number D', min_value=0)
    numberE = forms.IntegerField(label='Number E', min_value=0)
