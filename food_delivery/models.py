from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from django.urls import reverse

# this contains all the food items that can be bought
class Food( models.Model):
    # name and description of food
    name = models.CharField( max_length= 75)
    description = models.TextField()

    # date to be updated every time this is updated
    datePosted = models.DateTimeField( auto_now= True)

    # created by the seller
    seller = models.ForeignKey( User, on_delete= models.CASCADE, default= 1)

    # making images required - Pillow needs to installed
    image = models.ImageField( blank= False, null= True, upload_to= 'foods')

    # MRP of the item
    price = models.DecimalField( max_digits= 5, decimal_places= 2)

    # discount on the item
    discount = models.DecimalField( max_digits= 5, decimal_places= 2)

    # quantity available
    quantity = models.IntegerField( default= 0)

    # ingredients used by the user
    ingredients = models.TextField( default= 'Details not provided by Chef')

    @property
    def isAvailable( self):
        return self.quantity > 0

    @property
    def actualValue( self):
        return self.price - self.discount

    def __str__(self):
        return self.name
        # return '{}: {}\nAvailable for Rs.{} after discount of Rs.{}'.format( self.name, self.description, self.price - self.discount, self.discount)
    
    def get_absolute_url(self):
        return reverse( 'food-delivery-food-detail', kwargs={'pk':self.pk})