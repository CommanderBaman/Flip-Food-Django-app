from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# forms for registering and updating information
from .forms import UserRegisterationForm, UserUpdateForm, ProfileUpdateForm

# to prevent some pages from being opened up because of not logged in
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

# getting 404 page
from django.shortcuts import get_object_or_404

# used for registering users
def register( request):
    if request.method == 'POST':
        form = UserRegisterationForm( request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get( 'username')
            messages.success( request, 'Account created for {}! Please Login below.'.format( username))
            return redirect( 'users-login')
    else:
        form = UserRegisterationForm()

    context = {
        'form': form
    }
    return render( request, 'users/register.html', context)

# used for displaying users
@login_required
def profile( request):
    if request.method == 'POST':
        userUpdateForm = UserUpdateForm( request.POST, instance= request.user)
        profileUpdateForm = ProfileUpdateForm( 
            request.POST, # for updating with the post data
            request.FILES, # for updating the image 
            instance= request.user.profile
        )

        if userUpdateForm.is_valid() and profileUpdateForm.is_valid():
            userUpdateForm.save()
            profileUpdateForm.save()
            messages.success( request, 'Your account information was updated!')
            return redirect( 'users-profile')


    else:
        userUpdateForm = UserUpdateForm( instance= request.user)
        profileUpdateForm = ProfileUpdateForm( instance= request.user.profile)

    context = {
        'userUpdateForm' : userUpdateForm, 
        'profileUpdateForm': profileUpdateForm, 
    }
    return render( request, 'users/profile.html', context)

# for viewing profile by outside people
def profileViewer( request, sellerName):
    profile = get_object_or_404( User, username= sellerName)
    context = {
        'userProfile':profile, 
    }
    return render( request, 'users/profile-viewer.html', context)
