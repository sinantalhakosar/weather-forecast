from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator


class SignUpForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField()
    

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)