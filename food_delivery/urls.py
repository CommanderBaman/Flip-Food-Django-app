from django.urls import path, include
from . import views

urlpatterns = [
    path( '', views.main, name='food-delivery-home'),
    path( 'about/', views.about, name='food-delivery-about'),
    path( 'cart/', views.cart, name='food-delivery-cart'),
    path( 'checkout/', views.checkout, name='food-delivery-checkout'),
    path( 'confirmed/', views.confirmed, name='food-delivery-confirmed'),
]
