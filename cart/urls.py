from django.urls import path
from . import views

urlpatterns = [
    path( 'cart/', views.cart, name='cart-cart'),
    path( 'checkout/', views.checkout, name='cart-checkout'),
    path( 'confirmed/', views.confirmed, name='cart-confirmed'),
    path( 'cart/create/<int:foodPK>/', views.createFoodItem, name='cart-cart-create-item'),
    path( 'cart/<int:foodPK>/<int:toIncrease>/', views.quantityHandle, name='cart-cart-quantity-handler'),
    path( 'cart/delete/', views.deleteCart, name='cart-cart-delete'),
]