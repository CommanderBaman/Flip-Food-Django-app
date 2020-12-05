from django.urls import path
from . import views

urlpatterns = [
	path( "", views.index, name="solar-meter-input"),
]