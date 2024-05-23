from django.db import models
import string
import random


# FOR UNIQUE ROOM CODE RANDOM Generator
def generate_unique_code():
  length = 6

  while True:
    code =''.join(random.choices(string.ascii_uppercase, k=length))
    if Room.objects.filter(code=code).count() == 0: # check yung nasa class Room, i-filter niya isa isa and then i count yung mga same values ng code. if nag equal sa 0 it means that code is unique, so we stop the while loop and then return the unique random code.
      break

  return code

# Create your models here. PUT MOST OF YOUR LOGICS ON MODELS
class Room(models.Model):
  code = models.CharField(max_length=8, default="", unique=True)
  host = models.CharField(max_length=50, unique=True)
  guest_can_pause = models.BooleanField(null=False, default=False)
  votes_to_skip = models.IntegerField(null=False, default=1)
  created_at = models.DateTimeField(auto_now_add=True)
  
