# creating forms here
 
from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterationForm( UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]


class UserUpdateForm( forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

# form for profile
from .models import Profile

class ProfileUpdateForm( forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']


#forms for Address
from .models import Address

class AddressUpdateForm( forms.ModelForm):

    class Meta:
        model = Address
        fields = ['city', 'state', 'pin', 'localityAddress']