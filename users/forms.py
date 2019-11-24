from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    # the class meta - gives a nested namespace for configuration,
    #    in one place
    # specify the model that we want this form to interact with
    # and the fields that we want to be shown in the form,
    #  and in what order
    class Meta:
        model = User
        fields = [ 'username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = [ 'username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
