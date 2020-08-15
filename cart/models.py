from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from food_delivery.models import Food

class Cart( models.Model):
	# consists of many food items all pooled together
	buyer = models.OneToOneField( User, on_delete= models.CASCADE)
	# date to be updated every time this is updated
	datePosted = models.DateTimeField( auto_now= True)

	def __str__(self):
		return "Cart of {}".format( self.buyer.username)
	
	@property
	def totalCost(self):
		cost = 0
		for foodSelected in self.foodinfo_set.all():
			cost += foodSelected.foodCost
		return cost

	@property
	def totalSavings(self):
		save = 0
		for foodSelected in self.foodinfo_set.all():
			save += foodSelected.foodSave
		return save


class FoodInfo( models.Model):
	# contains info about a single food
	quantity = models.IntegerField( default= 1)
	cartRef = models.ForeignKey( Cart, on_delete= models.CASCADE, null= True)
	food = models.ForeignKey( Food, on_delete= models.CASCADE, null= True)

	def __str__(self):
		return "{} units of {} : {}".format( self.quantity, self.food.name, self.cartRef.buyer)
	
	@property
	def foodCost(self):
		return self.food.actualValue * self.quantity
	
	@property
	def foodSave(self):
		# savings on the particular thing
		return self.food.discount * self.quantity
	
	def increaseQuantity(self, value= 1):
		self.quantity += value 
		print( self.quantity)
		self.save()
		print( self.quantity)
		return "code run"
	
	def decreaseQuantity(self, value= 1):
		self.quantity -= value
		self.save()
		if self.quantity <= 0:
			self.delete()

	# def save(self, *args, **kwargs):
	# 	if self.id != self.cartRef.foodinfo_set.get( self.food.id).id:
	# 		oldObject = self.cartRef.foodinfo_set.get( self.food.id)
	# 		oldObject.increaseQuantity( value= self.quantity)
	# 		oldObject.save()
	# 	else:
	# 		super().save( *args, **kwargs)