from django import forms 
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from .models import Profile,Bank_details

class UserRegisterForm(UserCreationForm):
     email =  forms.EmailField()
 
     class Meta:
         #specify the model we want the form to interact with
         model = User
         fields = ['username', 'email', 'password1','password2']


class UserUpdateForm(forms.ModelForm):
    email =  forms.EmailField()
 
    class Meta:
        #specify the model we want the form to interact with 
         model = User
         fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
         model = Profile
         fields = ['image']



class BankDetailsForm(forms.Form):
    docfile  = forms.FileField(label = 'Select a file',help_text= 'max. 42 megabytes')