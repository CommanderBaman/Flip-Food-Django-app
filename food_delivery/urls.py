from django.urls import path
from . import views
from .views import ( 
    FoodListView, 
    FoodDetailView, 
    FoodCreateView,
    FoodUpdateView,
    FoodDeleteView 
)

urlpatterns = [
    path( '', FoodListView.as_view(), name='food-delivery-home'),
    path( 'food/<int:pk>', FoodDetailView.as_view(), name='food-delivery-food-detail'),
    path( 'food/new/', FoodCreateView.as_view(), name='food-delivery-create'),
    path( 'food/<int:pk>/update/', FoodUpdateView.as_view(), name='food-delivery-food-detail-update'),
    path( 'food/<int:pk>/delete/', FoodDeleteView.as_view(), name='food-delivery-food-delete'),
    path( 'about/', views.about, name='food-delivery-about'),
]
