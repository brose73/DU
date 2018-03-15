"""
Author: Brandon Rose
Date: 03-09-18
Class: ICT 4370
Assignment#: 9
Description: Django form for user registration
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .pass_validator import validate_pass

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    phone = forms.CharField(max_length=11, required=True, help_text='Required.')
    address = forms.CharField(max_length=50, required=True, help_text='Required.')
    address2 = forms.CharField(max_length=50, required=False, help_text='Optional.')
    town = forms.CharField(max_length=11, required=True, help_text='Required.')
    zip = forms.CharField(max_length=5, required=True, help_text='Required.')
    state = forms.CharField(max_length=11, required=True, help_text='Required.')
    password1 = forms.CharField(validators=[validate_pass])

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone', 'address', 'address2', 'town', 'zip', 'state', 'password1', 'password2', )
