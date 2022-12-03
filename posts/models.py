from django.db import models
from users.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="post_images/")
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='post_user', on_delete = models.CASCADE)
    
    def __str__(self):
        return f'Загаловок: {self.title}, Описание: {self.description}'
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
    