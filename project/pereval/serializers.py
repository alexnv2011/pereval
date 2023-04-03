from .models import *
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from drf_writable_nested import UniqueFieldsMixin, WritableNestedModelSerializer


class AuthorSerializer(ModelSerializer):
   # author_pereval = PerevalSerializer(many=True)  # show perevals for author

    class Meta:
        model = Author
        fields = '__all__' # ('email', 'first_name', 'last_name', 'otc')


class CoordsSerializer(ModelSerializer):

    class Meta:
        model = Coords
        fields = ('__all__') # ('latitude', 'longitude', 'height')



class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class PerevalSerializer(WritableNestedModelSerializer, ModelSerializer):
    #author = AuthorSerializer(read_only=True)
    coords = CoordsSerializer()
    images = ImageSerializer(source='image_set', many=True, read_only=True)

    class Meta:
        model = Pereval
        fields = '__all__'
