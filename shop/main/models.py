from django.db import models


class Card(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='cards/')
    created_at = models.DateTimeField()


class User(models.Model):
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    birth_day = models.IntegerField(null=True)
    birth_month = models.IntegerField(null=True)
    birth_year = models.IntegerField(null=True)
    password_hash = models.CharField(max_length=255)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    refresh_token = models.CharField(max_length=255, null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
