""" users Forms"""

from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class SignupForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())
    confirmation = forms.CharField(max_length=30, widget=forms.PasswordInput())

