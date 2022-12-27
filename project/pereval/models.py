from django.db import models


class Pereval(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    beauty_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255)
    connect = models.CharField(max_length=255)
    winter = models.CharField(max_length=50)
    summer = models.CharField(max_length=50)
    autumn = models.CharField(max_length=50)
    spring = models.CharField(max_length=50)

    def __str__(self):
        return f'Pereval: {str(self.pk)} - {self.title}'


class Coord(models.Model):
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    height = models.IntegerField(default=0)

    def __str__(self):
        return f' {str(self.latitude)} : {str(self.longitude)} : {str(self.height)}'


class Image(models.Model):
    title = models.CharField(max_length=255)
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE)

    def __str__(self):
        return f'Image: {str(self.pk)} - {self.title}'
