from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import *
from .serializers import *

class BuildingList(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class NodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Node.objects.all()
    serializer_class = NodeSerializerWithData

class AccelerometerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Accelerometer.objects.all()
    serializer_class= AccelerometerWithDataSerializer
