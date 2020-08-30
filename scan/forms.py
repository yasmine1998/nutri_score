from django import forms

class Codeform(forms.Form):
    code = forms.CharField(label='code')