from .models import *
from rest_framework import serializers
from drf_writable_nested import UniqueFieldsMixin, WritableNestedModelSerializer


class AuthorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')


class CoordsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Coords
        fields = ('latitude', 'longitude', 'height')



class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class PerevalSerializer(WritableNestedModelSerializer, serializers.HyperlinkedModelSerializer):
    author = AuthorSerializer()
    coords = CoordsSerializer()
    images = ImageSerializer(source='image_set', many=True, read_only=True)

    class Meta:
        model = Pereval
        fields = '__all__'


