from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserMessenger(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(verbose_name='Фото профиля', blank=True)
    about_me = models.TextField(verbose_name='О себе', max_length=1024, blank=True)

class Text(models.Model):
    user = models.ForeignKey(UserMessenger)
    text = models.TextField(max_length=512)

class Room(models.Model):
    users = models.ManyToManyField(UserMessenger)
    text = models.ForeignKey(Text, on_delete=models.CASCADE)
