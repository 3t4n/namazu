from rest_framework import serializers
from drf_queryfields import QueryFieldsMixin
from .models import *

class AccelerationComponentSerializer(serializers.ModelSerializer): 
    class Meta:
        model = AccelerationComponent
        fields = ('AccelerometerTime','XValue','YValue','ZValue')


class AccelerometerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accelerometer
        fields = ('id','MemoryAddress','Status')  

class AccelerometerWithDataSerializer(serializers.ModelSerializer):
    Data = AccelerationComponentSerializer(many=True)
    class Meta:
        model = Accelerometer
        fields = ('id','MemoryAddress','Status','Data')  

class NodeSerializer(serializers.ModelSerializer):
    Accelerometers = AccelerometerSerializer(many=True)
    class Meta:
        model = Node
        fields = ('id','UserId','Shared','Synced','PingTime','Accelerometers')

class NodeSerializerWithData(NodeSerializer):
    Accelerometers = AccelerometerWithDataSerializer(many=True)    

class GroupNodesSerializer(serializers.ModelSerializer):
    Nodes = NodeSerializer(many=True)
    class Meta:
        model = GroupNodes
        fields = ('id','Name','Nodes')

class BuildingSerializer(serializers.ModelSerializer, QueryFieldsMixin):
    GroupsNodes = GroupNodesSerializer(many=True)
    class Meta:
        model = Building
        fields = ('id','Name','GpsLatitude','GroupsNodes')







