from django.shortcuts import render, redirect, get_object_or_404

# Create your views here

# for adding the login required condition on funtions
from django.contrib.auth.decorators import login_required
from food_delivery.models import Food
from django.contrib import messages

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
    context = {
        'foodInfos': foodInfos
    }
    messages.warning( request, "This is a dummy site - meaning it will not send you food. But the transaction link below is real and will cost you. Please leave if you think you are ordering actual food.")
    return render( request, 'cart/checkout.html', context)

# returns the confirmation that the order is ordered
@login_required
def confirmed( request):
    context = {}
    return render( request, 'cart/confirmed.html', context)
