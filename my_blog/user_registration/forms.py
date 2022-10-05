from dataclasses import fields
from django import forms
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from pkg_resources import require

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']