from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    profile_image = models.ImageField(
        upload_to='user_profile_image/'
    )
    phone = models.CharField(
        max_length=50
    )
    description = models.CharField(max_length=200, blank=True, null=True)
    
class Follows(models.Model):
    from_user = models.ForeignKey(
        User,
        related_name='follow_user',
        on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        User,
        related_name='following_user',
        on_delete=models.CASCADE
    )