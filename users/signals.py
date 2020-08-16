# for directly adding the profile things without going to the admin page
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# define sender and receiver
from django.dispatch import receiver 
from .models import Profile

@receiver( post_save, sender= User)
def create_profile( sender, instance, created, **kwargs):
    if created:
        Profile.objects.create( user= instance)


@receiver( post_save, sender= User)
def save_profile( sender, instance, **kwargs):
    instance.profile.save()

    # creating an address item on save of profile
    if kwargs['created']:
        addressItem = instance.profile.address_set.create( profile= instance.profile)
        addressItem.save()
