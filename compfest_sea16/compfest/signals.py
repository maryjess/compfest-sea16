import uuid
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import User

@receiver(pre_save, sender=User)
def set_random_user_id(sender, instance, **kwargs):
    if not instance.user_id:
        instance.user_id = str(uuid.uuid4())