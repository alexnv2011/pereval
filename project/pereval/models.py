from django.db import models

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
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    height = models.IntegerField(default=0)
    status = models.TextField(max_length=20, choices=STATUSES, default=new)

    def __str__(self):
        return f'{str(self.pk)} - {self.title}'



class Image(models.Model):
    title = models.CharField(max_length=255)
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE)

    def __str__(self):
        return f'{str(self.pk)} - {self.title}'
