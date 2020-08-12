from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from .models import Food

from django.views.generic import ListView, DetailView


# main page of the food delivery system
class FoodListView(ListView):
    model = Food
    template_name = 'food_delivery/main.html'
    context_object_name = 'foods'
    ordering = ['-datePosted']

class FoodDetailView(DetailView):
    model = Food
    template_name = 'food_delivery/food-detail.html'
    context_object_name = 'food'

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

