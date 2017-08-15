from django import forms


class LoginForm(forms.Form):
    """docstring for LoginForm"""
    userName = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
