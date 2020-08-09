from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

# main page of the food delivery system
def main( request):
    context = {}
    return render( request, 'food_delivery/main.html', context)

# shows the about us page
def about( request):
    context = {}
    return render( request, 'food_delivery/about.html', context)

#shows the cart of the user 
def cart( request):
    context = {}
    return render( request, 'food_delivery/cart.html', context)

#shows the checkout page - contains payment option and estimated delivery time
def checkout( request):
    context = {}
    return render( request, 'food_delivery/checkout.html', context)

# returns the confirmation that the order is ordered
def confirmed( request):
    context = {}
    return render( request, 'food_delivery/confirmed.html', context)