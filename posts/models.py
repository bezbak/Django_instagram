from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="post_images/")
    created = models.DateTimeField(auto_now_add=True)
