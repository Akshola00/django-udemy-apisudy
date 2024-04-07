from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Movieserializer
from .models import Moviedata
# Create your views here.
#  apu endpoint sallow you to tgive diffrent results to the end user by chnaging theur urls
class Movieviewset(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = Movieserializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='action')
    serializer_class = Movieserializer


class ComedyViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='comedy')
    serializer_class = Movieserializer

