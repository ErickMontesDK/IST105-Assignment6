from django import forms

class NumbersForm(forms.Form):
    numberA = forms.IntegerField(label='Number A')
    numberB = forms.IntegerField(label='Number B')
    numberC = forms.IntegerField(label='Number C')
    numberD = forms.IntegerField(label='Number D')
    numberE = forms.IntegerField(label='Number E')
