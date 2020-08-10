from django.db import models

# Create your models here.

# this contains all the food items that can be bought
class Food( models.Model):
    # name and description of food
    name = models.CharField( max_length= 75)
    description = models.CharField( max_length= 200)

    # making images required - Pillow needs to installed
    image = models.ImageField( blank= False, null= True, upload_to= 'foods')

    # MRP of the item
    price = models.DecimalField( max_digits= 5, decimal_places= 2)

    # discount on the item
    discount = models.DecimalField( max_digits= 5, decimal_places= 2)

    # quantity available
    quantity = models.IntegerField( default= 0)

    @property
    def isAvailable( self):
        return self.quantity > 0

    def __str__(self):
        return self.name
        # return '{}: {}\nAvailable for Rs.{} after discount of Rs.{}'.format( self.name, self.description, self.price - self.discount, self.discount)
    
    