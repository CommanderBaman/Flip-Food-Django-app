from django.shortcuts import render

# Create your views here.

# used for registering users
def register( request):
    context = {}
    return render( request, 'users/register.html', context)

# used for logging in users
def login( request):
    context = {}
    return render( request, 'users/login.html', context)