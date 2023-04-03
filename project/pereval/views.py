from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.utils.dateparse import parse_date
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import QueryDict
from rest_framework.response import Response
from rest_framework import status


class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    http_method_names = ['get', 'post', 'retrieve', 'put', 'patch']


class PerevalViewset(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    http_method_names = ['get', 'post', 'retrieve', 'put', 'patch']

    def create(self, request, *args, **kwargs):

        if Author.objects.filter(email=request.data.get("email")).exists():
            author = Author.objects.get(email=request.data.get("email"))
        else:
            author = Author()
            author.email = request.data.get("email")
            author.otc = request.data.get("otc")
            author.first_name = request.data.get("first_name")
            author.last_name = request.data.get("last_name")
            author.save()

        request.data._mutable = True
        request.data['author'] = author.pk  # set correct author
        request.data._mutable = False

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ImageViewset(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


