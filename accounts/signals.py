from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Manager

@receiver(post_save, sender=User)
def create_manager_profile(sender, instance, created, **kwargs):
    print("Signal fired for:", instance.email, instance.role)
    if created and instance.role == 'manager':
        Manager.objects.get_or_create(user=instance)