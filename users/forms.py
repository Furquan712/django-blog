from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class meta:
        model = User
        field = ['username', 'email', 'password1' , 'password2']
       