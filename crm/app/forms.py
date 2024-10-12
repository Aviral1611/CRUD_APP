from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput,TextInput
from .models import Customer

#- Register/ Create a user

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1','password2']


#- Login a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# Add a record
class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name','email','phone','address','city','province','country']


class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name','email','phone','address','city','province','country']