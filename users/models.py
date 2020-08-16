from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from PIL import Image

import json, requests

class Profile( models.Model):
    user = models.OneToOneField( User, on_delete= models.CASCADE)
    image = models.ImageField( default= 'profile_pics/default-profile-pic.jpg', upload_to= 'profile_pics')
    

    def __str__( self):
        return "{}'s Profile".format( self.user.username)
    
    def save( self, *args, **kwargs):
        super().save( *args, **kwargs)

        # resizing image to fit the template better
        imageSaved = Image.open( self.image.path)
        outputSize = ( 360, int(360 * imageSaved.height / imageSaved.width))
        imageSaved.resize( outputSize)
        imageSaved.save( self.image.path)


class Address( models.Model):
    # linking to profile
    profile = models.ForeignKey( Profile, on_delete= models.CASCADE, default= 1)
    # loading cities
    cityJSONfile = 'https://raw.githubusercontent.com/nshntarora/Indian-Cities-JSON/master/cities.json'
    res = requests.get( cityJSONfile)
    cityDict = json.loads( res.text)
    cityChoices = [( str( city["state"]), str( city["name"])) for city in cityDict]

    city = models.CharField( max_length= 120, choices= cityChoices, default='Your city here')

    # loading states
    stateChoices = set([( str( state["state"]), str( state["state"])) for state in cityDict])
    # stateChoices = set( stateChoices)
    state = models.CharField( max_length= 120, choices= stateChoices, default= 'Your state here')

    # PIN number of the city the person is living in
    pin = models.IntegerField( default= 160019)

    # address line
    localityAddress = models.TextField( max_length= 180, default= 'Your local address here', help_text="Enter your house number and the society name here")

    def __str__(self):
        return "{}'s Address - Line {}".format( self.profile.user.username, self.id)

