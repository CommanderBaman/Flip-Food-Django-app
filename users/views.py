from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# forms for registering and updating information
from .forms import ( 
    UserRegisterationForm, 
    UserUpdateForm, 
    ProfileUpdateForm, 
    AddressUpdateForm
)

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
            messages.success( request, 'Account for {} was created successfully! Please Login below to complete the process'.format(username))
            return redirect( 'users-register-profile')
    else:
        form = UserRegisterationForm()

    context = {
        'form': form,
    }
    return render( request, 'users/register.html', context)

# profile register
@login_required
def profileRegister( request):
    if request.method == 'POST':
        form = ProfileUpdateForm(
            request.POST, # for updating with the post data
            request.FILES, # for updating the image 
            instance= request.user.profile
        )
        form2 = AddressUpdateForm(
            request.POST, # for updating with the post data
            request.FILES, # for updating the image 
            instance= request.user.profile
        )
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            # username = form.cleaned_data.get( 'username')
            messages.success( request, 'Your account was created successfully! Let\'s eat food.')
            return redirect( 'food-delivery-home')
    else:
        form = ProfileUpdateForm()
        form2 = AddressUpdateForm()

    context = {
        'form': form,
        'form2': form2,
    }
    return render( request, 'users/profile-register.html', context)

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
        addressUpdateForm = AddressUpdateForm( 
            request.POST, # for updating with the post data
            # request.FILES, # for updating the image 
            instance= request.user.profile.address_set.get( profile= request.user.profile)
        )

        if userUpdateForm.is_valid() and profileUpdateForm.is_valid() and addressUpdateForm.is_valid():
            userUpdateForm.save()
            profileUpdateForm.save()
            addressUpdateForm.save()
            messages.success( request, 'Your account information was updated!')
            return redirect( 'users-profile')


    else:
        userUpdateForm = UserUpdateForm( instance= request.user)
        profileUpdateForm = ProfileUpdateForm( instance= request.user.profile)
        addressUpdateForm = AddressUpdateForm( instance= request.user.profile.address_set.get( profile= request.user.profile))

    context = {
        'userUpdateForm' : userUpdateForm, 
        'profileUpdateForm': profileUpdateForm, 
        'addressUpdateForm': addressUpdateForm, 
    }
    return render( request, 'users/profile.html', context)

# for viewing profile by outside people
def profileViewer( request, userPK):
    profile = get_object_or_404( User, pk = userPK)
    context = {
        'userProfile':profile, 
        'userAddress': profile,
    }
    return render( request, 'users/profile-viewer.html', context)
