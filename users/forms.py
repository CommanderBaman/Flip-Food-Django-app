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
    
    def clean(self, *args, **kwargs):
        cleaned_data = super().clean( *args, **kwargs)
        city = cleaned_data.get( 'city')
        state = cleaned_data.get( 'state')


        # using form validation
        import json, requests
        cityJSONfile = 'https://raw.githubusercontent.com/nshntarora/Indian-Cities-JSON/master/cities.json'
        res = requests.get( cityJSONfile)
        cityDict = json.loads( res.text)

        for info in cityDict:
            if city == info['name']:
                # checking for correct state and city
                if state != info['state']:
                    raise forms.ValidationError("Please enter a correct combination of State and City")
        
        
        # couldn't find a combination for pincode and city so left it

                
                
            

        



        