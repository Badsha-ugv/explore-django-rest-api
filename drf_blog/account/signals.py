from django.conf import settings 
from django.db.models.signals import post_save 
from django.dispatch import receiver 

from django.contrib.auth.models import User 
from rest_framework.authtoken.models import Token 


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_auth_token(sender, instance, created=None, **kwargs):
    if created:
        Token.objects.create(user=instance)