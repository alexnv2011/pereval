from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.exceptions import NON_FIELD_ERRORS
"""
Models for classes: Pereval, Author, Coords, Image.
"""

new = 'new'
pending = 'pending'
accepted = 'accepted'
rejected = 'rejected'


STATUSES = [
    (new, 'Новый'),
    (pending, 'На рассмотрении'),
    (accepted, 'Принят'),
    (rejected, 'Отклонен')
]


# User._meta.get_field('email')._unique = True


class Author(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    otc = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.email


class Coords(models.Model):
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    height = models.IntegerField(default=0)

    def __str__(self):
        return f'lat {str(self.latitude)} : lon {str(self.longitude)} : h {str(self.height)}'

class Pereval(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    beauty_title = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255, null=True, blank=True)
    connect = models.CharField(max_length=255, null=True, blank=True)
    winter = models.CharField(max_length=50, null=True, blank=True)
    summer = models.CharField(max_length=50, null=True, blank=True)
    autumn = models.CharField(max_length=50, null=True, blank=True)
    spring = models.CharField(max_length=50, null=True, blank=True)
    status = models.TextField(max_length=20, choices=STATUSES, default=new)
    coords = models.OneToOneField(Coords, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, related_name='author_pereval', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'pk:{str(self.pk)} - {self.title}'



class Image(models.Model):
    title = models.CharField(max_length=255)
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='%Y/%m/%d/', null=True, max_length=255)

    def __str__(self):
        return f'{str(self.pk)} - {self.title}'

