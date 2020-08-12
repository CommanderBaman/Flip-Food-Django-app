from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from PIL import Image

class Profile( models.Model):
    user = models.OneToOneField( User, on_delete= models.CASCADE)
    image = models.ImageField( default= 'profile_pics/default-profile-pic.jpg', upload_to= 'profile_pics')
    

    def __str__( self):
        return "{}'s Profile".format( self.user.username)
    
    def save( self):
        super().save()

        # resizing image to fit the template better
        imageSaved = Image.open( self.image.path)
        outputSize = ( 360, 360 * imageSaved.height / imageSaved.width)
        imageSaved.thumbnail( outputSize)
        imageSaved.save( self.image.path)
