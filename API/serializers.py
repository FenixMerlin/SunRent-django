from rest_framework import serializers
from DB.models import*


class ScooterSerializer(serializers.ModelSerializer):
  class Meta:
    model = Scooter
    fields = ['identifier', 'battery_percentage']

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['first_name']

class MissionSerializer(serializers.ModelSerializer):
  scooter = ScooterSerializer()
  user = UserSerializer()
  
  class Meta:
    model = Mission
    fields = ['scooter', 'user', 'prioriti']


