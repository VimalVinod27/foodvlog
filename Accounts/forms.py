from django import forms

class RegForm(forms.Form):
    first_name=forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)
    username = forms.CharField(max_length=200)
    password1 = forms.CharField(max_length=200)
    password2 = forms.CharField(max_length=200)


class LoginForm(forms.Form):
    username=forms.CharField(max_length=200)
    password=forms.CharField(max_length=200)

