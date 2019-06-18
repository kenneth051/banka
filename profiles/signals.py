from api.models import User
from profiles.models import Profiles
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save,sender=User)
def create_profile(sender,instance, created, **kwargs):
    if created:
        profile=Profiles.objects.create(user=instance)
        profile.save()

