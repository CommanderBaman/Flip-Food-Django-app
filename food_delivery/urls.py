from django.urls import path, include
from . import views
from .views import FoodListView, FoodDetailView

urlpatterns = [
    path( '', FoodListView.as_view(), name='food-delivery-home'),
    path( 'food/<int:pk>', FoodDetailView.as_view(), name='food-delivery-food-detail'),
    path( 'about/', views.about, name='food-delivery-about'),
    path( 'cart/', views.cart, name='food-delivery-cart'),
    path( 'checkout/', views.checkout, name='food-delivery-checkout'),
    path( 'confirmed/', views.confirmed, name='food-delivery-confirmed'),
]
