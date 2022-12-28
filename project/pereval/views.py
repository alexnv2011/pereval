from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.utils.dateparse import parse_date
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import *


class PerevalViewset(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer


class ImageViewset(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


# Получение данных из БД
def index(request):
    perevals = Pereval.objects.all()
    return render(request, "index.html", {"perevals": perevals})


