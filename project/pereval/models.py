from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


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


User._meta.get_field('email')._unique = True


class Coords(models.Model):
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    height = models.IntegerField(default=0)

    def __str__(self):
        return f'lat {str(self.latitude)} : lon {str(self.longitude)} : h {str(self.height)}'

class Pereval(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    beauty_title = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255, null=True)
    connect = models.CharField(max_length=255, null=True)
    winter = models.CharField(max_length=50, null=True)
    summer = models.CharField(max_length=50, null=True)
    autumn = models.CharField(max_length=50, null=True)
    spring = models.CharField(max_length=50, null=True)
    status = models.TextField(max_length=20, choices=STATUSES, default=new)
    coords = models.OneToOneField(Coords, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{str(self.pk)} - {self.title}'



class Image(models.Model):
    title = models.CharField(max_length=255)
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photo/%Y/%m/%d/', null=True, max_length=255)

    def __str__(self):
        return f'{str(self.pk)} - {self.title}'
