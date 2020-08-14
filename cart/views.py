from django.shortcuts import render

# Create your views here

# for adding the login required condition on funtions
from django.contrib.auth.decorators import login_required


#shows the cart of the user 
@login_required
def cart( request):
    context = {}
    return render( request, 'cart/cart.html', context)

#shows the checkout page - contains payment option and estimated delivery time
@login_required
def checkout( request):
    context = {}
    return render( request, 'cart/checkout.html', context)

# returns the confirmation that the order is ordered
@login_required
def confirmed( request):
    context = {}
    return render( request, 'cart/confirmed.html', context)
