from django.urls import path
from . import views

urlpatterns = [
    path( 'cart/', views.cart, name='cart-cart'),
    path( 'checkout/', views.checkout, name='cart-checkout'),
    path( 'confirmed/', views.confirmed, name='cart-confirmed'),
    path( 'cart/create/<int:foodPK>/', views.createFoodItem, name='cart-cart-create-item'),
    path( 'cart/create/<int:foodPK>/<int:pageNumber>/', views.createFoodItemPaginated, name='cart-cart-create-item-paginated'),
    path( 'cart/<int:foodPK>/<int:toIncrease>/<int:toMain>/', views.quantityHandle, name='cart-cart-quantity-handler'),
    path( 'cart/delete/', views.deleteCart, name='cart-cart-delete'),
]