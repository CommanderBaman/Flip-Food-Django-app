from django.shortcuts import render, redirect, get_object_or_404

# Create your views here

# for adding the login required condition on funtions
from django.contrib.auth.decorators import login_required
from food_delivery.models import Food
from django.contrib import messages

from datetime import datetime, timedelta

#shows the cart of the user 
@login_required
def cart( request):
    context = {
        'foodInfos': request.user.cart.foodinfo_set.all()
    }
    return render( request, 'cart/cart.html', context)

# increases or decreases the contents of a cart of a user
@login_required
def quantityHandle( request, foodPK, toIncrease, toMain= 0):
    foodToChange = get_object_or_404( request.user.cart.foodinfo_set, pk= foodPK )
    # print(foodToChange)
    # foodToChange = request.user.cart.foodinfo_set.get( pk = foodPK)
    # print(foodToChange)
    if toIncrease:
        foodToChange.increaseQuantity()
    else:
        foodToChange.decreaseQuantity()

    if toMain:
        return redirect( 'food-delivery-home')
    return redirect('cart-cart')

# delete all the food items related to the cart
@login_required
def deleteCart( request):
    for foodInfo in request.user.cart.foodinfo_set.all():
        foodInfo.delete()
    return redirect('cart-cart')

# create food item for cart 
@login_required
def createFoodItem( request, foodPK):
    foodItem = request.user.cart.foodinfo_set.create( food= Food.objects.get( pk= foodPK))
    foodItem.save()

    return redirect( 'food-delivery-home')

# create food item for cart - but page is paginated
@login_required
def createFoodItemPaginated( request, foodPK, pageNumber):
    foodItem = request.user.cart.foodinfo_set.create( food= Food.objects.get( pk= foodPK))
    foodItem.save()

    return redirect( 'food-delivery-home', page_number = pageNumber)

#shows the checkout page - contains payment option and estimated delivery time
@login_required
def checkout( request):
    try:
        foodInfos = request.user.cart.foodinfo_set.all()
    except:
        messages.error( request, 'Please add something to your cart before proceeding to payment!')
        return redirect( 'food-delivery-home')

    try:
        userAddress = request.user.profile.address_set.all()[0]
    except:
        messages.error( request, 'Looks like you haven\'t added your address till now. Let\'s update it below.')
        return redirect( 'users-register-profile')

    context = {
        'foodInfos': foodInfos, 
        'userAddress': userAddress,
    }
    messages.warning( request, "This is a dummy site - meaning it will not send you food. But the transaction link below is real and will cost you. Please leave if you think you are ordering actual food.")
    return render( request, 'cart/checkout.html', context)

# returns the confirmation that the order is ordered
@login_required
def confirmed( request):
    today = datetime.now()
    deliveryDay = today + timedelta( days= 3)
    try:
        foodInfos = request.user.cart.foodinfo_set.all()
        foodInfo = foodInfos[0]
        messages.success( request, 'Food Ordered! Food to arrive in 3 days. Happy Meal.')
        userAddress = request.user.profile.address_set.all()[0]
        context = {
            'foodInfos': foodInfos,
            'todayDate': datetime.now().strftime("%d %B, %Y %H:%M:%S"), 
            'deliveryDate': deliveryDay.strftime("%d %B, %Y"),
            'userAddress': userAddress,
        }
        return render( request, 'cart/confirmed.html', context)
    except:
        messages.info( request, 'Whoa! Mistake from our side. Please keep browsing.')
        return redirect( 'food-delivery-home')

# transferring to home page after the payment with deletion of objects
@login_required
def confirmedDelete( request):
    for foodInfo in request.user.cart.foodinfo_set.all():
        foodInfo.delete()
    
    messages.success( request, 'Your order is ordered. It is arriving in 3 days!')
    return redirect('food-delivery-home')
    
