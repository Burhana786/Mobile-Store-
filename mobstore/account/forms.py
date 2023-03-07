from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'first_name','last_name','email','username','password1','password2','phone','address','usertype'
        ]


class SigninForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput(),max_length=100)  