from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import *
from .serializers import *
from .pagination import *

class BuildingList(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class NodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Node.objects.all()
    serializer_class = NodeSerializerWithData

class AccelerometerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Accelerometer.objects.all()
    serializer_class= AccelerometerWithDataSerializer

class AccelerationComponentsList(generics.ListCreateAPIView):
    serializer_class = AccelerationComponentSerializer
    pagination_class = ComponentsPagination
    def get_queryset(self):
        idu = self.kwargs["idu"] 
        return AccelerationComponent.objects.filter(AccelerometerId=idu).order_by('-id')
