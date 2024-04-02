from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Movieserializer
from .models import Moviedata
# Create your views here.
class Movieviewset(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = Movieserializer
    