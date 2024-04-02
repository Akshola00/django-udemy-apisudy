from rest_framework import serializers
from .models import Moviedata

#creating youir serializers
class Movieserializer(serializers.ModelSerializer):
    class Meta:
        model = Moviedata
        fields= ['id', 'name', 'duration', 'rating']