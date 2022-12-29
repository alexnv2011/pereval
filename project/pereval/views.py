from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.utils.dateparse import parse_date
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import *
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import viewsets

class PerevalViewset(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer


class ImageViewset(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


# Создание и сохранение перевала в БД
def create(request):
    if request.method == "POST":
        pereval = Pereval()
        pereval.title = request.POST.get('title')
        pereval.beauty_title = request.POST.get("beauty_title")
        pereval.other_titles = request.POST.get("other_titles")
        pereval.connect = request.POST.get("connect")
        pereval.winter = request.POST.get("winter")
        pereval.summer = request.POST.get("summer")
        pereval.autumn = request.POST.get("autumn")
        pereval.spring = request.POST.get("spring")

        coords = Coords()
        coords.latitude = request.POST.get("latitude")
        coords.longitude = request.POST.get("longitude")
        coords.height = request.POST.get("height")

        pereval.coords = coords

        author = User()
        author.email = request.POST.get("email")
        author.username = request.POST.get("username")
        author.first_name = request.POST.get("first_name")
        author.last_name = request.POST.get("last_name")

        pereval.author = author

        pereval.save()
        return Response(request.data, status=status.HTTP_201_CREATED)
    else:
        return Response(request.data, status=status.HTTP_400_BAD_REQUEST)


# class PhotoList(APIView):
#     def post(self, request, format=None):
#         serializer = ImageSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # Получение данных из БД
# def index(request):
#     perevals = Pereval.objects.all()
#     return render(request, "index.html", {"perevals": perevals})


