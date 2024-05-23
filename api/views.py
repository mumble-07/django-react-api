from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# Create your views here.

# def main(request):
#   return HttpResponse("<h1>Hello World</h1>")

class RoomView(generics.CreateAPIView):
# class RoomView(generics.ListAPIView): #create a room CreateAPIView, ListAPIView
  queryset = Room.objects.all() # what we want to return
  serializer_class = RoomSerializer # json format(?)
  