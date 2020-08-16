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
        outputSize = ( 360, 360 * imageSaved.height / imageSaved.width)
        imageSaved.resize( outputSize)
        imageSaved.save( self.image.path)


class Address( models.Model):
    # linking to profile
    profile = models.ForeignKey( Profile, on_delete= models.CASCADE)
    # loading cities
    cityJSONfile = 'https://raw.githubusercontent.com/nshntarora/Indian-Cities-JSON/master/cities.json'
    res = requests.get( cityJSONfile)
    cityDict = json.loads( res.text)
    cityChoices = [( str( city["name"]), str( city["state"])) for city in cityDict]

    city = models.CharField( max_length= 120, choices= cityChoices)

    # loading states
    stateChoices = [( str( state["state"]), "India") for state in cityDict]
    state = models.CharField( max_length= 120, choices= stateChoices)

    # PIN number of the city the person is living in
    pin = models.IntegerField()

    # address line
    localityAddress = models.TextField( max_length= 180)

    def __str__(self):
        return "{}'s Address - Line {}".format( self.profile.user.username, self.id)

