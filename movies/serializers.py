from rest_framework import serializers
from .models import Moviedata

#creating youir serializers
class Movieserializer(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None,use_url=True) 
    class Meta:
        model = Moviedata
        fields= ['id', 'name', 'duration', 'rating', 'typ', 'image']