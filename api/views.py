from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# Create your views here.

# def main(request):
#   return HttpResponse("<h1>Hello World</h1>")
  
class RoomView(generics.CreateAPIView): #create a room CreateAPIView, ListAPIView
  queryset = Room.objects.all()
  serializer_class = RoomSerializer
  