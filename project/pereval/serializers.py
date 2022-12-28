from .models import *
from rest_framework import serializers


class PerevalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pereval
        fields = ['id', 'title', 'date_added', 'beauty_title', 'title', 'other_titles',
                  'connect', 'winter', 'summer', 'autumn', 'spring', 'latitude', 'longitude', 'height', 'status']


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'title', ]
