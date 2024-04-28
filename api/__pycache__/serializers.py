from rest_framework import serializers
from .model import Room

class RoomSerializer(serializers.ModelSerializer):
  class Meta:
    model = Room
    fields = ('id', 'code', 'host', 'guest_')