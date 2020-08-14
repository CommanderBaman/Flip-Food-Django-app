from django.urls import path
from . import views

urlpatterns = [
    path( 'cart/', views.cart, name='cart-cart'),
    path( 'checkout/', views.checkout, name='cart-checkout'),
    path( 'confirmed/', views.confirmed, name='cart-confirmed'),
]